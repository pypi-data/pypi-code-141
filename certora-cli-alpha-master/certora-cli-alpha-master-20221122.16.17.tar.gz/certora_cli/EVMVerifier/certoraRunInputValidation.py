

import os
import string
import sys
import argparse
import logging
import itertools
import shutil
import time
import re
import subprocess
from typing import Dict, List, Tuple, Any, Set, Optional
import json
from pathlib import Path
from copy import deepcopy

scripts_dir_path = Path(__file__).parent.resolve()  # containing directory
sys.path.insert(0, str(scripts_dir_path))

from EVMVerifier.certoraDualArg import check_arg_and_setting_consistency
from Shared.certoraUtils import get_certora_root_directory, get_trivial_contract_name
from Shared.certoraUtils import DEFAULT_CLOUD_ENV, DEFAULT_STAGING_ENV
from Shared.certoraUtils import as_posix, PUBLIC_KEY, red_text, LEGAL_CERTORA_KEY_LENGTHS
from Shared.certoraUtils import PACKAGE_FILE, abs_posix_path_obj, is_windows
from Shared.certoraUtils import Mode, get_closest_strings, DEFAULT_SOLC


# logger for issues regarding argument parsing and user input validation
validation_logger = logging.getLogger("validation")

CL_ARGS = ""

def warn_verify_file_args(files: List[str]) -> Tuple[Set[str], Set[str], Dict[str, str], Dict[str, Set[str]]]:
    """
    Verifies all file inputs are legal. If they are not, throws an exception.
    If there are any redundancies or duplication, warns the user.
    Otherwise, it returns a set of all legal contract names.
    @param files: A list of string of form: [contract.sol[:contract_name] ...]
    @return: (contracts, files, contract_to_file, file_to_contracts)
        contracts - a set of contract names
        files - a set of paths to files containing contracts
        contract_to_file - a mapping from contract name -> file containing it
        file_to_contracts - a mapping from a file path -> name of the contracts within it we verify
    """

    """
    The logic is complex, and better shown by examples.
    Legal use cases:
    1. A.sol B.sol
        ->  contracts=(A, B), files=(A.sol, B.sol), contract_to_file={'A': 'A.sol', 'B': 'B.sol'},
            file_to_contracts = {'A.sol': ['A'], 'B.sol': ['B']}
    2. A.sol:a B.sol:b C.sol
        ->  contracts=(a, b, C), files=(A.sol, B.sol, C.sol),
            contract_to_file={'a': 'A.sol', 'b': 'B.sol', 'C': 'C.sol'},
            file_to_contracts = {'A.sol': ['a'], 'B.sol': ['b'], 'C.sol': ['C']}
    3. A.sol:B B.sol:c
        ->  contracts=(B, c), files=(A.sol, B.sol),
            contract_to_file={'B': 'A.sol', 'c': 'B.sol'},
            file_to_contracts = {'A.sol': ['B'], 'B.sol': ['c']}
    4. A.sol:b A.sol:c
        ->  contracts=(b, c), files=(A.sol),
            contract_to_file={'b': 'A.sol', 'c': 'A.sol'},
            file_to_contracts = {'A.sol': ['b', 'c']}

    Warning cases:
    4. A.sol A.sol
        -> A.sol is redundant
    5. A.sol:a A.sol:a
        -> A.sol:a is redundant
    6. A.sol:A
        -> contract name A is redundant (it's the default name)

    Illegal cases:
    7. A.sol:a B.sol:a
        -> The same contract name cannot be used twice
    8. ../A.sol A.sol
        -> The same contract name cannot be used twice
    9. A.sol:B B.sol
        -> The same contract name cannot be used twice
    10. A.sol:a A.sol
        -> The same file cannot contain two different contracts
    11. A.sol A.sol:a
        -> The same file cannot contain two different contracts

    Warning are printed only if the input is legal
    @raise argparse.ArgumentTypeError in an illegal case (see above)
    """
    if len(files) == 1 and (files[0].endswith(".conf") or files[0].endswith(".tac")):
        return set(), set(), dict(), dict()  # No legal contract names

    declared_contracts = set()
    file_paths = set()
    all_warnings = set()

    contract_to_file: Dict[str, str] = dict()
    file_to_contracts: Dict[str, Set[str]] = dict()

    for f in files:

        default_contract_name = get_trivial_contract_name(f)
        posix_path = os.path.relpath(abs_posix_path_obj(f), Path.cwd())
        assert posix_path.count(':') < 2
        if ':' in posix_path:
            filepath_str, contract_name = posix_path.split(":")
            if contract_name == default_contract_name:
                all_warnings.add(f"contract name {contract_name} is the same as the file name and can be omitted "
                                 f"from {filepath_str}:{contract_name}")
        else:
            filepath_str = posix_path
            contract_name = default_contract_name

        if filepath_str in file_to_contracts:
            if contract_name in file_to_contracts[filepath_str]:
                all_warnings.add(f"file argument {f} appears more than once and is redundant")
                continue

        if contract_name in contract_to_file and contract_to_file[contract_name] != filepath_str:
            # A.sol:a B.sol:a
            raise argparse.ArgumentTypeError(f"A contract named {contract_name} was declared twice for files "
                                             f"{contract_to_file[contract_name]}, {filepath_str}")

        contract_to_file[contract_name] = filepath_str
        file_to_contracts.setdefault(filepath_str, set()).add(contract_name)
        declared_contracts.add(contract_name)
        file_paths.add(filepath_str)

    for warning in all_warnings:
        validation_logger.warning(warning)

    return declared_contracts, file_paths, contract_to_file, file_to_contracts

def check_contract_name_arg_inputs(args: argparse.Namespace) -> None:
    """
    This function verifies that all options that expect to get contract names get valid contract names.
    If they do, nothing happens. If there is any error, an exception is thrown.
    @param args: Namespace containing all command line arguments, generated by get_args()
    @raise argparse.ArgumentTypeError if a contract name argument was expected, but not given.
    """
    contract_names, file_paths, contract_to_file, file_to_contract = warn_verify_file_args(args.files)
    args.contracts = contract_names
    args.file_paths = file_paths
    args.file_to_contract = file_to_contract
    args.contract_to_file = contract_to_file

    # we print the warnings at the end of this function, only if no errors were found. Each warning appears only once
    all_warnings = set()

    # Link arguments can be either: contractName:slot=contractName
    #   or contractName:slot=integer(decimal or hexadecimal)
    if args.link is not None:
        for link in args.link:
            executable = link.split(':')[0]
            executable = get_trivial_contract_name(executable)
            if executable not in contract_names:
                __suggest_contract_name(f"link {link} doesn't match any contract name", executable, contract_names,
                                        contract_to_file)

            library_or_const = link.split('=')[1]
            try:
                parsed_int = int(library_or_const, 0)  # can be either a decimal or hexadecimal number
                if parsed_int < 0:
                    raise argparse.ArgumentTypeError(f"slot number is negative at {link}")
            except ValueError:
                library_name = get_trivial_contract_name(library_or_const)
                if library_name not in contract_names:
                    __suggest_contract_name(f"{library_name} in link {link} doesn't match any contract name",
                                            library_name, contract_names, contract_to_file)

        check_conflicting_link_args(args)

    args.verified_contract_files = []
    if args.assert_contracts is not None:
        for assert_arg in args.assert_contracts:
            contract = get_trivial_contract_name(assert_arg)
            if contract not in contract_names:
                __suggest_contract_name(f"--assert argument {contract} doesn't match any contract name", contract,
                                        contract_names, contract_to_file)
            else:
                args.verified_contract_files.append(contract_to_file[contract])

    args.spec_files = None

    if args.verify is not None:
        spec_files = set()
        for ver_arg in args.verify:
            contract, spec = ver_arg.split(':')
            contract = get_trivial_contract_name(contract)
            if contract not in contract_names:
                __suggest_contract_name(f"--verify argument {contract} doesn't match any contract name", contract,
                                        contract_names, contract_to_file)
            spec_files.add(spec)
            args.verified_contract_files.append(contract_to_file[contract])
        args.spec_files = sorted(list(spec_files))

    contract_to_address = dict()
    if args.address:
        for address_str in args.address:
            contract = address_str.split(':')[0]
            if contract not in contract_names:
                __suggest_contract_name(f"unrecognized contract in --address argument {address_str}", contract,
                                        contract_names, contract_to_file)
            number = address_str.split(':')[1]
            if contract not in contract_to_address:
                contract_to_address[contract] = number
            elif contract_to_address[contract] != number:
                raise argparse.ArgumentTypeError(f'contract {contract} was given two different addresses: '
                                                 f'{contract_to_address[contract]} and {number}')
            else:
                all_warnings.add(f'address {number} for contract {contract} defined twice')
    args.address = contract_to_address

    if args.struct_link:
        contract_slot_to_contract = dict()
        for link in args.struct_link:
            location = link.split('=')[0]
            destination = link.split('=')[1]
            origin = location.split(":")[0]
            if origin not in contract_names:
                __suggest_contract_name(
                    f"--structLink argument {link} is illegal: {origin} is not a defined contract name", origin,
                    contract_names, contract_to_file)
            if destination not in contract_names:
                __suggest_contract_name(
                    f"--structLink argument {link} is illegal: {destination} is not a defined contract name",
                    destination, contract_names, contract_to_file)

            if location not in contract_slot_to_contract:
                contract_slot_to_contract[location] = destination
            elif contract_slot_to_contract[location] == destination:
                all_warnings.add(f"--structLink argument {link} appeared more than once")
            else:
                raise argparse.ArgumentTypeError(f"{location} has two different definitions in --structLink: "
                                                 f"{contract_slot_to_contract[location]} and {destination}")

    for warning in all_warnings:
        validation_logger.warning(warning)


def check_mode_of_operation(args: argparse.Namespace) -> None:
    """
    Ascertains we have only one mode of operation in use and updates args.mode to store it as an enum.
    The modes are:
    1. There is a single .tac file
    2. There is a single .conf file
    3. There is a single .json file
    4. --assert
    5. --verify
    6. --bytecode - the only case in which files may be empty


    This function ascertains there is no overlap between the modes. The correctness of each mode is checked in other
    functions.
    @param args: A namespace including all CLI arguments provided
    @raise an argparse.ArgumentTypeError when:
        1. .conf|.tac|.json file is used with --assert|--verify flags
        2. when both --assert and --verify flags were given
        3. when the file is not .tac|.conf|.json and neither --assert nor --verify were used
        4. If any file is provided with --bytecode flag
        5. If either --bytecode or --bytecode_spec was used without the other.
    """
    is_verifying = args.verify is not None and len(args.verify) > 0
    is_asserting = args.assert_contracts is not None and len(args.assert_contracts) > 0
    is_bytecode = args.bytecode_jsons is not None and len(args.bytecode_jsons) > 0
    has_bytecode_spec = args.bytecode_spec is not None

    if is_verifying and is_asserting:
        raise argparse.ArgumentTypeError("only one option of --assert and --verify can be used")

    special_file_type = None

    if len(args.files) > 0 and is_bytecode:
        raise argparse.ArgumentTypeError("Cannot use --bytecode with other files")

    if len(args.files) == 0 and not is_bytecode:
        raise argparse.ArgumentTypeError("Should always provide input files, unless --bytecode is used")

    if has_bytecode_spec != is_bytecode:
        raise argparse.ArgumentTypeError("Must use --bytecode together with --bytecode_spec")

    if len(args.files) == 1:
        # We already checked that this is the only case where we might encounter CONF or TAC files
        input_file = args.files[0]
        for suffix in [".tac", ".conf", ".json"]:
            if input_file.endswith(suffix):
                special_file_type = suffix

        if special_file_type is not None:
            if is_verifying:
                raise argparse.ArgumentTypeError(
                    f"Option --verify cannot be used with a {special_file_type} file {input_file}")
            if is_asserting:
                raise argparse.ArgumentTypeError(
                    f"Option --assert cannot be used with a {special_file_type} file {input_file}")

    if special_file_type is None and not is_asserting and not is_verifying and not is_bytecode:
        raise argparse.ArgumentTypeError(
            "You must use either --assert or --verify or --bytecode when running the Certora Prover")

    # If we made it here, exactly a single mode was used. We update the namespace entry mode accordingly:
    if is_verifying:
        args.mode = Mode.VERIFY
    elif is_asserting:
        args.mode = Mode.ASSERT
    elif is_bytecode:
        args.mode = Mode.BYTECODE
    elif special_file_type == '.conf':
        args.mode = Mode.CONF
    elif special_file_type == '.tac':
        args.mode = Mode.TAC
    elif special_file_type == '.json':
        args.mode = Mode.REPLAY
    else:
        raise ValueError(f"File {input_file} has unsupported file type {special_file_type}")


def check_packages_arguments(args: argparse.Namespace) -> None:
    """
    Performs checks on the --packages_path and --packages options.
    @param args: A namespace including all CLI arguments provided
    @raise an argparse.ArgumentTypeError if:
        1. both options --packages_path and --packages options were used
        2. in --packages the same name was given multiples paths
    """
    if args.packages_path is None:
        args.packages_path = os.getenv("NODE_PATH", f"{Path.cwd() / 'node_modules'}")
        validation_logger.debug(f"args.packages_path is {args.packages_path}")

    if args.packages is not None and len(args.packages) > 0:
        args.package_name_to_path = dict()
        for package_str in args.packages:
            package = package_str.split("=")[0]
            path = package_str.split("=")[1]
            if not Path(path).is_dir():
                raise argparse.ArgumentTypeError(
                    f"package path {path} is not a directory")
            if package in args.package_name_to_path:
                raise argparse.ArgumentTypeError(
                    f"package {package} was given two paths: {args.package_name_to_path[package]}, {path}")
            if path.endswith("/"):
                # emitting a warning here because here loggers are already initialized
                validation_logger.warning(
                    f"Package {package} is given a path ending with a `/`, which could confuse solc: {path}")
            args.package_name_to_path[package] = path

        args.packages = sorted(args.packages, key=str.lower)

    else:
        if not PACKAGE_FILE.exists():
            validation_logger.warning(
                f"Default package file {PACKAGE_FILE} not found, external contract dependencies could be unresolved. "
                f"Ignore if solc invocation was successful")
        elif not os.access(PACKAGE_FILE, os.R_OK):
            validation_logger.warning(f"No read permissions for default package file {PACKAGE_FILE}")
        else:
            try:
                with PACKAGE_FILE.open() as package_json_file:
                    package_json = json.load(package_json_file)
                    deps = set(list(package_json["dependencies"].keys()) if "dependencies" in package_json else
                               list(package_json["devDependencies"].keys()) if "devDependencies" in package_json
                               else list())  # May need both

                    packages_path = args.packages_path
                    packages_to_path_list = [f"{package}={packages_path}/{package}" for package in deps]
                    args.packages = sorted(packages_to_path_list, key=str.lower)

            except EnvironmentError:
                ex_type, ex_value, _ = sys.exc_info()
                validation_logger.warning(f"Failed in processing {PACKAGE_FILE}: {ex_type}, {ex_value}")


def check_deployment_args(args: argparse.Namespace) -> None:
    """
    Checks that the user didn't choose both --staging and --cloud
    @param args: A namespace including all CLI arguments provided
    @raise argparse.ArgumentTypeError if both --staging and --cloud options are present in args
    """
    if args.staging:
        if args.cloud:
            raise argparse.ArgumentTypeError("cannot use both --staging and --cloud")
        args.env = DEFAULT_STAGING_ENV
    else:
        args.env = DEFAULT_CLOUD_ENV


def check_solc_solc_map(args: argparse.Namespace) -> None:
    """
    Executes all post-parsing checks of --solc and --solc_map arguments:
    1. --solc and --solc_map cannot be used together
    2. If both --solc and --solc_map were not used, and we are not in conf file mode,
       take the default solc and check its validity.
    3. If --solc_map is used and we are not in .conf file mode:
       verify that every source file appears in the map and that every mapping has a valid file path as a
       key. Note: we rely on type_solc_map() to guarantee that no file appears with conflicting values in the map
    For backwards compatibility reasons, we also allow the entry of contract names instead of files. If so, we fetch the
    source file that includes the contract and map it. We again check that there are no conflicts.
    @param args: A namespace including all CLI arguments provided
    @raise argparse.ArgumentTypeError if:
                1. both --solc and --solc_map options are present in args
                2. A key in the solc mapping is not a valid source file or a valid contract name
                3. Some source files do not appear as keys in the solc map
                4. If there are two or more contracts in the same source file with conflicting values
    """
    if args.solc is not None and args.solc_map is not None:
        raise argparse.ArgumentTypeError("You cannot use both --solc and --solc_map arguments")

    if args.solc_map is None:
        args.solc = is_solc_file_valid(args.solc)
    else:  # we use solc_map, check its validity
        orphan_files = deepcopy(args.file_paths)
        normalized_solc_map = deepcopy(args.solc_map)  # The normalized map has only file paths as keys, not contracts

        for (source_file, solc) in args.solc_map.items():
            # No need to call is_solc_file_valid(solc) as they are validated as a part of type_solc_map()
            abs_src_file = str(Path(source_file).resolve())
            src_file_found = False
            for _file in args.file_paths:
                curr_abs_src_file = str(Path(_file).resolve())
                if abs_src_file == curr_abs_src_file:
                    if _file in orphan_files:
                        orphan_files.remove(_file)
                        src_file_found = True
                        break

            if not src_file_found:
                # it might be a contract name, for backwards compatibility reasons
                contract = source_file
                if contract not in args.contracts:
                    raise argparse.ArgumentTypeError(
                        f"--solc_map argument {source_file}={solc}: {source_file} is not a source file")
                containing_source_file = args.contract_to_file[contract]
                if containing_source_file in normalized_solc_map:
                    if normalized_solc_map[containing_source_file] != solc:
                        raise argparse.ArgumentTypeError(
                            f"Source file {containing_source_file} has two conflicting Solidity compiler versions in "
                            f"--solc_map, one of them is {contract}={solc}")
                else:
                    normalized_solc_map[containing_source_file] = solc
                    del normalized_solc_map[contract]
                    orphan_files.remove(containing_source_file)

        if len(orphan_files) > 0:
            raise argparse.ArgumentTypeError(
                f"Some source files do not appear in --solc_map: {', '.join(orphan_files)}")

        args.solc_map = normalized_solc_map


def check_optimize_map(args: argparse.Namespace) -> None:
    """
    Executes all post-parsing checks of --optimize_map and --optimize arguments:
    1. --optimize and --optimize_map cannot be used together
    2. if --optimize_map is used and we are not in .conf file mode:
       Verify that every source file appears exactly once in the map and that every mapping has a valid source file as a
       key. Note: we rely on type_optimize_map() to guarantee that no source file appears with conflicting values.
       Note: for backwards compatibility reasons, we allow using contract names as keys. It is not allowed to have two
       or more different contracts from the same source file with different optimizations.
    @param args: A namespace including all CLI arguments provided
    @raise argparse.ArgumentTypeError if:
                1. Both --optimize and --optimize_map options are present in args.
                2. A key in the mapping is not a valid source file or contract.
                3. Some source files do not appear as keys in the map and none of their contracts appear as keys either.
                4. No file has two or more contracts with conflicting optimization values.
    """
    if args.optimize is not None and args.optimize_map is not None:
        raise argparse.ArgumentTypeError("You cannot use both --optimize and --optimize_map arguments")

    if args.optimize_map is not None:

        # See if any source file is missing a number of runs in the map
        orphan_files = deepcopy(args.file_paths)
        normalized_opt_map = deepcopy(args.optimize_map)  # The normalized map has only file paths as keys not contracts

        for (source_file, num_runs) in args.optimize_map.items():
            abs_src_file = str(Path(source_file).resolve())
            src_file_found = False
            for _file in args.file_paths:
                curr_abs_src_file = str(Path(_file).resolve())
                if abs_src_file == curr_abs_src_file:
                    if _file in orphan_files:
                        orphan_files.remove(_file)
                        src_file_found = True
                        break

            if not src_file_found:
                # it might be a contract name, for backwards compatibility reasons
                contract = source_file
                if contract not in args.contracts:
                    raise argparse.ArgumentTypeError(
                        f"--optimize_map argument {source_file}={num_runs}: {source_file} is not a source file")
                containing_source_file = args.contract_to_file[contract]
                if containing_source_file in normalized_opt_map:
                    if normalized_opt_map[containing_source_file] != num_runs:
                        raise argparse.ArgumentTypeError(
                            f"Source file {containing_source_file} has two conflicting number of runs optimizations in "
                            f"--optimize_map, one of them is {contract}={num_runs}")
                else:
                    normalized_opt_map[containing_source_file] = num_runs
                    del normalized_opt_map[contract]
                    orphan_files.remove(containing_source_file)

        if len(orphan_files) > 0:
            raise argparse.ArgumentTypeError(
                f"Some source files do not appear in --optimize_map: {', '.join(orphan_files)}")

        # See that there is no --optimize_runs inside --solc_args
        if args.solc_args is not None:
            if '--optimize-runs' in args.solc_args:
                raise argparse.ArgumentTypeError(
                    "You cannot use both --optimize_map and the --solc_args argument --optimize-runs")

        args.optimize_map = normalized_opt_map


def handle_optimize(args: argparse.Namespace) -> None:
    """
    Checks that there are no conflicts between --optimize and --solc_args. If all is good, adds the necessary number of
    runs to solc_args.
    --optimize 800 should be identical to --solc_args '["--optimize", "--optimize-runs", "800"]'. We convert from
    --optimize to --solc_args in this function, unless there is an error.

    We throw on the following errors:
    * If the number of runs between --optimize and --solc_args does not agree
    * --solc_args '["--optimize", "--optimize-runs", "800"]' is malformed AND we use --optimize

    We ignore the following errors:
    * --solc_args '["--optimize", "--optimize-runs", "800"]' is malformed and we DO NOT use --optimize: solc would catch

    It is not considered an error if the number of runs between --optimize and --solc_args agrees, but we warn about
    the redundancy
    """
    if args.solc_args is not None and args.optimize is not None:
        if '--optimize' in args.solc_args:
            if '--optimize-runs' in args.solc_args:
                opt_runs_idx = args.solc_args.index('--optimize-runs')
                num_runs_idx = opt_runs_idx + 1
                if len(args.solc_args) < num_runs_idx:
                    raise argparse.ArgumentTypeError(
                        "solc argument --optimize-runs must be provided an integer value")
                num_runs = args.solc_args[num_runs_idx]
                try:
                    num_runs = int(num_runs)
                except ValueError:
                    raise argparse.ArgumentTypeError("solc argument --optimize-runs must be provided an integer value")
                if num_runs != int(args.optimize):
                    raise argparse.ArgumentTypeError(f"The number of runs to optimize for in --optimize {args.optimize}"
                                                     f" does not agree with solc argument --optimize-runs {num_runs}")
            else:
                '''
                Default number of runs is 200
                https://solidity-fr.readthedocs.io/fr/latest/using-the-compiler.html
                '''
                num_runs = 200
                if num_runs != int(args.optimize):
                    raise argparse.ArgumentTypeError(f"The number of runs to optimize for in --optimize {args.optimize}"
                                                     f" does not agree with solc argument --optimize "
                                                     f"(default of 200 runs)")

            validation_logger.warning("Using solc arguments --optimize (and --optimize-runs) is redundant when"
                                      " using certoraRun argument --optimize")
        elif '--optimize-runs' in args.solc_args:
            raise argparse.ArgumentTypeError("solc argument --optimize-runs must appear with solc argument --optimize")
        else:  # Neither --optimize nor --optimize-runs are in --solc_args
            args.solc_args += ["--optimize", "--optimize-runs", f"{args.optimize}"]
    elif args.optimize is not None:
        # arg.solc_args is None
        args.solc_args = ["--optimize", "--optimize-runs", f"{args.optimize}"]


def check_rule(args: argparse.Namespace) -> None:
    """
    Checks that we do not use both --rule (or --settings -rule) in any other mode than --verify
    @param args: a namespace containing command line arguments
    @raises ArgumentTypeError when a user chose a rule with --rule or --settings -rule when not in verify mode
    """
    if args.rule is None:
        return

    if not args.verify and args.bytecode_spec is None:
        raise argparse.ArgumentTypeError(
            "checking for a specific rule is only supported with --verify and --bytecode_spec")


class UniqueStore(argparse.Action):
    """
    This class makes the argparser throw an error for a given flag if it was inserted more than once
    """

    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: Any,  # type: ignore
                 option_string: str) -> None:
        if getattr(namespace, self.dest, self.default) is not self.default:
            parser.error(f"{option_string} appears several times.")
        setattr(namespace, self.dest, values)


def check_args_post_argparse(args: argparse.Namespace) -> None:
    """
    Performs checks over the arguments after basic argparse parsing

    argparse parses option one by one. This is the function that checks all relations between different options and
    arguments. We assume here that basic syntax was already checked.
    @param args: A namespace including all CLI arguments provided
    @raise argparse.ArgumentTypeError if input is illegal
    """
    if args.path is None:
        args.path = str(__default_path())
    check_files_input(args.files)
    check_contract_name_arg_inputs(args)  # Here args.contracts is set
    check_packages_arguments(args)
    check_solc_solc_map(args)
    check_optimize_map(args)
    check_arg_and_setting_consistency(args)
    check_rule(args)
    certora_root_dir = as_posix(get_certora_root_directory())
    default_jar_path = Path(certora_root_dir) / "emv.jar"
    if args.jar is not None or \
            (default_jar_path.is_file() and args.staging is None and args.cloud is None):
        args.local = True
    else:
        args.local = False
        check_deployment_args(args)

    if args.java_args is not None:
        args.java_args = ' '.join(args.java_args).replace('"', '')

    if args.typecheck_only and args.disableLocalTypeChecking:
        raise argparse.ArgumentTypeError("cannot use both --typecheck_only and --disableLocalTypeChecking")

    if args.typecheck_only and args.build_only:
        raise argparse.ArgumentTypeError("cannot use both --typecheck_only and --build_only")

    if args.local and args.typecheck_only:
        raise argparse.ArgumentTypeError("cannot use --typecheck_only in local tool runs")

    if args.send_only:
        if args.local:
            validation_logger.warning("--send_only has no effect in local tool runs")

        if args.short_output:
            validation_logger.warning("When using --send_only, --short_output is automatically enabled; "
                                      "--short_output in the command line is redundant")
        else:
            args.short_output = True

    if args.optimize:
        handle_optimize(args)

    if args.debug is None and args.debug_topics:
        raise argparse.ArgumentTypeError("cannot use --debug_topics without --debug")
    if isinstance(args.msg, str):
        msg = args.msg.strip('"')
        if len(msg) > 256:
            raise argparse.ArgumentTypeError("--msg can't accept a message longer than 256 chars")
        # the allowed characters are:
        # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789=, ':.\\-/\\\\"_
        whitelist = string.ascii_letters + string.digits + "=, ':.\\-/\\\\_"
        for c in msg:
            if c not in whitelist:
                raise argparse.ArgumentTypeError(f"{c} isn't an allowed character")


def __default_path() -> Path:
    path = Path.cwd() / "contracts"
    if path.is_dir():
        return path.resolve()
    return Path.cwd().resolve()


def __check_no_pretty_quotes(args_list: List[str]) -> None:
    """
    :param args_list: A list of CL arguments
    :raises argparse.ArgumentTypeError if there are wrong quotation marks “ in use (" are the correct ones)
    """
    for arg in args_list:
        if '“' in arg:
            raise argparse.ArgumentTypeError('Please replace “ with " quotation marks')


def __suggest_contract_name(err_msg: str, contract_name: str, all_contract_names: Set[str],
                            contract_to_file: Dict[str, str]) -> None:
    err_str = err_msg
    suggestions = get_closest_strings(contract_name, list(all_contract_names), max_suggestions=1)

    if len(suggestions) == 1:
        suggested_contract = suggestions[0]
        err_str = f'{err_str}. Maybe you meant contract {suggested_contract} ' \
                  f'(found in file {contract_to_file[suggested_contract]})?'
    err_str += ' \nNote: To specify a contract in a differently-named sol file, you can ' \
               'provide the contract name explicitly, ie: certoraRun sol_file.sol:XYZcontract ' \
               '--verify XYZcontract:spec_file.spec'

    """
    Why do we raise from None?
    We run this function from an except block. We explicitly want to discard the context of the exception caught in the
    wrapping except block. If we do not discard the previous exception context, we see the following confusing pattern:
        "During handling of the above exception, another exception occurred:"
    """
    raise argparse.ArgumentTypeError(err_str) from None  # ignore prev exception context


def check_conflicting_link_args(args: argparse.Namespace) -> None:
    """
    Detects contradicting definitions of slots in link and throws.
    DOES NOT check for file existence, format legality, or anything else.
    We assume the links contain no duplications.
    @param args: A namespace, where args.link includes a list of strings that are the link arguments
    @raise argparse.ArgumentTypeError if a slot was given two different definitions
    """
    pair_list = itertools.permutations(args.link, 2)
    for pair in pair_list:
        link_a = pair[0]
        link_b = pair[1]
        slot_a = link_a.split('=')[0]
        slot_b = link_b.split('=')[0]
        if slot_a == slot_b:
            raise argparse.ArgumentTypeError(f"slot {slot_a} was defined multiple times: {link_a}, {link_b}")


def is_solc_file_valid(orig_filename: Optional[str]) -> str:
    """
    Verifies that a given --solc argument is valid:
        1. The file exists
        2. We have executable permissions for it
    :param orig_filename: Path to a solc executable file. If it is None, a default path is used instead,
                          which is also checked
    :return: Default solc executable if orig_filename was None, orig_filename is returned otherwise
    :raises argparse.ArgumentTypeException if the argument is invalid (including the default if it is used)
    """
    if orig_filename is None:
        filename = DEFAULT_SOLC
        err_prefix = f'No --solc path given, but default solidity executable {DEFAULT_SOLC} had an error. '
    else:
        filename = orig_filename
        err_prefix = ''

    if is_windows() and not filename.endswith(".exe"):
        filename += ".exe"

    common_mistakes_suffixes = ['sol', 'conf', 'tac', 'spec', 'cvl']
    for suffix in common_mistakes_suffixes:
        if filename.endswith(f".{suffix}"):
            raise argparse.ArgumentTypeError(f"wrong Solidity executable given: {filename}")

    # see https://docs.python.org/3.8/library/shutil.html#shutil.which. We use no mask to give a precise error
    solc_location = shutil.which(filename, os.F_OK)
    if solc_location is not None:
        solc_path = Path(solc_location)
        if solc_path.is_dir():
            raise argparse.ArgumentTypeError(
                err_prefix + f"Solidity executable {filename} is a directory not a file: {solc_path}")
        if not os.access(solc_path, os.X_OK):
            raise argparse.ArgumentTypeError(
                err_prefix + f"No execution permissions for Solidity executable {filename} at {solc_path}")
        return solc_path.as_posix()

    # given solc executable not found in path. Looking if the default solc exists
    if filename != DEFAULT_SOLC:
        default_solc_path = shutil.which(DEFAULT_SOLC)  # If it is not None, the file exists and is executable
        if default_solc_path is not None:
            try:
                run_res = subprocess.check_output([default_solc_path, '--version'], shell=False)
                default_solc_version = run_res.decode().splitlines()[-1]
            except Exception as e:
                # If we cannot invoke this command, we should not recommend the executable to the user
                validation_logger.debug(f"Could not find the version of the default Solidity compiler {DEFAULT_SOLC}\n"
                                        f"{e}")
                default_solc_version = None

            if default_solc_version is not None:
                err_msg = f"Solidity executable {orig_filename} not found in path.\n" \
                          f"The default Solidity compiler was found at {default_solc_path} " \
                          f"with version {default_solc_version}. To use it, remove the --solc argument:\n"

                split_cl_args = CL_ARGS.split()
                solc_index = split_cl_args.index("--solc")
                # solc must be followed by a file name
                solc_less_args = split_cl_args[0:solc_index] + split_cl_args[solc_index + 2:]
                new_cl = ' '.join(solc_less_args)
                err_msg += f'cerotraRun.py {new_cl}'

                raise argparse.ArgumentTypeError(err_msg)

    # Couldn't find the given solc nor the default solc
    raise argparse.ArgumentTypeError(err_prefix + f"Solidity executable {filename} not found in path")


def validate_certora_key() -> str:
    """
    Checks that the environment variable CERTORAKEY is legal and returns a valid Certora key.
    If the environment variable CERTORAKEY is undefined or empty, the public key is returned.
    If the environment variable CERTORAKEY has a different legal value, returns it.
    @raise RuntimeError if CERTORAKEY has an illegal value.
    """
    key = os.environ.get("CERTORAKEY", "")
    if not key:
        key = PUBLIC_KEY
        print('\n')
        txt_1 = "You are using the demo version of the tool. Therefore, the tool has limited resources."
        validation_logger.warning(f'{red_text(txt_1)}')
        txt_2 = 'If you have a premium Certora key, please set it as the environment variable CERTORAKEY.'
        validation_logger.warning(f"{red_text(txt_2)}\n")
        time.sleep(1)

    if not re.match(r'^[0-9A-Fa-f]+$', key):  # checks if the key is a hexadecimal number (without leading 0x)
        raise RuntimeError("environment variable CERTORAKEY has an illegal value")
    if not len(key) in LEGAL_CERTORA_KEY_LENGTHS:
        raise RuntimeError("environment variable CERTORAKEY has an illegal length")
    return key


def check_files_input(file_list: List[str]) -> None:
    """
    Verifies that correct input was inserted as input to files.
    As argparser verifies the files exist and the correctness of the format, we only check if only a single operation
    mode was used.
    The allowed disjoint cases are:
    1. Use a single .conf file
    2. Use a single .tac file
    3. Use any number of [contract.sol:nickname ...] (at least one is guaranteed by argparser)
    @param file_list: A list of strings representing file paths
    @raise argparse.ArgumentTypeError if more than one of the modes above was used
    """
    num_files = len(file_list)
    if num_files > 1:  # if there is a single file, there cannot be a mix between file types
        for file in file_list:
            if '.tac' in file:
                raise argparse.ArgumentTypeError(f'When using the tool in TAC mode by providing .tac file {file}, '
                                                 f'you can only provide a single file. {num_files} files were given')
            if '.conf' in file:
                raise argparse.ArgumentTypeError(f'When using the tool in CONF mode by providing .conf file {file}, '
                                                 f'you can only provide a single file. {num_files} files were given')
