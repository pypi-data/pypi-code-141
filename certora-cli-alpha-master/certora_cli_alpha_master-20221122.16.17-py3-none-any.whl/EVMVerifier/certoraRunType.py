
import os
import argparse
import re
import ast
import logging
from typing import Dict, List, Optional, Any, NoReturn
import json
import shutil
from pathlib import Path
from Shared.certoraUtils import split_by_delimiter_and_ignore_character
from EVMVerifier.certoraRunInputValidation import is_solc_file_valid
type_logger = logging.getLogger("type")


def _raise_argument_type_error(msg: str) -> NoReturn:
    raise argparse.ArgumentTypeError(msg)


def type_non_negative_integer(string: str) -> str:
    """
    :param string: A string
    :return: The same string, if it represents a decimal integer
    :raises argparse.ArgumentTypeError if the string does not represent a non-negative decimal integer
    """
    if not string.isnumeric():
        _raise_argument_type_error(f'expected a non-negative integer, instead given {string}')
    return string


def type_positive_integer(string: str) -> str:
    type_non_negative_integer(string)
    if int(string) == 0:
        _raise_argument_type_error("Expected a positive number, got 0 instead")
    return string


def type_jar(filename: str) -> str:
    file_path = Path(filename)
    if not file_path.is_file():
        raise argparse.ArgumentTypeError(f"file {filename} does not exist.")
    if not os.access(filename, os.X_OK):
        raise argparse.ArgumentTypeError(f"no execute permission for jar file {filename}")

    basename = file_path.name  # extract file name from path.
    # NOTE: expects Linux file paths, all Windows file paths will fail the check below!
    if re.search(r"^[\w.-]+\.jar$", basename):
        # Base file name can contain only alphanumeric characters, underscores, or hyphens
        return filename

    raise argparse.ArgumentTypeError(f"file {filename} is not of type .jar")


def type_optional_readable_file(filename: str) -> str:
    """
    Verifies that if filename exists, it is a valid readable file.
    It is the responsibility of the consumer to check the file exists
    """
    file_path = Path(filename)
    if file_path.is_dir():
        raise argparse.ArgumentTypeError(f"{filename} is a directory and not a file")
    elif file_path.exists() and not os.access(filename, os.R_OK):
        raise argparse.ArgumentTypeError(f"no read permissions for {filename}")
    return filename  # It is okay if the file does not exist


def type_readable_file(filename: str) -> str:
    file_path = Path(filename)
    if not file_path.exists():
        raise argparse.ArgumentTypeError(f"file {filename} not found")
    if file_path.is_dir():
        raise argparse.ArgumentTypeError(f"{filename} is a directory and not a file")
    if not os.access(filename, os.R_OK):
        raise argparse.ArgumentTypeError(f"no read permissions for {filename}")
    return filename


def type_optimize_map(args: str) -> Dict[str, str]:
    """
    Checks that the argument is of form <contract_1>=<num_runs_1>,<contract_2>=<num_runs_2>,..
    and if all <num_runs> are valid positive integers.
    We also validate that a contract doesn't have more than a single value (but that value may appear multiple times.

    :param args: argument of --optimize_map
    :return: {contract: num_runs}.
             For example, if --optimize_args a=12 is used, returned value will be:
             {'a': '12'}
    :raises argparse.ArgumentTypeError if the format is wrong
    """
    args = args.replace(' ', '')  # remove whitespace

    '''
    Regex explanation:
    ([^=,]+=[^=,]+) describes a single key-value pair in the map. It must contain a single = sign, something before
    and something after
    We allow more than one, as long as all but the last are followed by a comma hence ([^=,]+=[^=,]+,)*
    We allow nothing else inside the argument, so all is wrapped by ^ and $
    '''
    optimize_matches = re.search(r'^([^=,]+=[^=,]+,)*([^=,]+=[^=,]+)$', args)

    if optimize_matches is None:
        raise argparse.ArgumentTypeError(f"--optimize_map argument {args} is of wrong format. Must be of format:"
                                         f"<contract>=<num_runs>[,..]")

    optimize_map = {}  # type: Dict[str, str]
    all_num_runs = set()  # If all --optimize_args use the same num runs, it is better to use --optimize, and we warn
    all_warnings = set()

    for match in args.split(','):
        contract, num_runs = match.split('=')
        type_non_negative_integer(num_runs)  # raises an exception if the number is bad
        if contract in optimize_map:
            if optimize_map[contract] == num_runs:
                all_warnings.add(f"optimization mapping {contract}={num_runs} appears multiple times and is redundant")
            else:
                raise argparse.ArgumentTypeError(f"contradicting definition in --optimize_map for contract {contract}: "
                                                 f"it was given two different numbers of runs to optimize for: "
                                                 f"{optimize_map[contract]} and {num_runs}")
        else:
            optimize_map[contract] = num_runs
            all_num_runs.add(num_runs)

    if len(all_num_runs) == 1:
        all_warnings.add(f'All contracts are optimized for the same number of runs in --optimize_map. '
                         f'--optimize {list(all_num_runs)[0]} can be used instead')

    for warning in all_warnings:
        type_logger.warning(warning)

    type_logger.debug(f"optimize_map = {optimize_map}", True)
    return optimize_map


def type_dir(dirname: str) -> str:
    dir_path = Path(dirname)
    if not dir_path.exists():
        raise argparse.ArgumentTypeError(f"path {dirname} does not exist")
    if dir_path.is_file():
        raise argparse.ArgumentTypeError(f"{dirname} is a file and not a directory")
    if not os.access(dirname, os.R_OK):
        raise argparse.ArgumentTypeError(f"no read permissions to {dirname}")
    return dir_path.resolve().as_posix()


def type_build_dir(path_str: str) -> str:
    """
    Verifies the argument is not a path to an existing file/directory and that a directory can be created at that
    location
    """
    try:
        p = Path(path_str)
        if p.exists():
            raise argparse.ArgumentTypeError(f"--build_dir {path_str} already exists")
        # make sure the directory can be created
        p.mkdir(parents=True)
        shutil.rmtree(path_str)
    except OSError:
        raise argparse.ArgumentTypeError(f"failed to create build directory - {path_str} ")

    return path_str

def type_tool_output_path(filename: str) -> str:
    file_path = Path(filename)
    if file_path.is_dir():
        raise argparse.ArgumentTypeError(f"--toolOutput {filename} is a directory")
    if file_path.is_file():
        type_logger.warning(f"--toolOutPut {filename} file already exists")
        if not os.access(filename, os.W_OK):
            raise argparse.ArgumentTypeError(f'No permission to rewrite --toolOutPut file {filename}')
    else:
        try:
            with file_path.open('w') as f:
                f.write('try')
            file_path.unlink()
        except (ValueError, IOError, OSError) as e:
            raise argparse.ArgumentTypeError(f"could not create --toolOutput file {filename}. Error: {e}")

    return filename


def type_list(candidate: str) -> List[str]:
    """
    Verifies the argument can be evaluated by python as a list
    """
    v = ast.literal_eval(candidate)
    if type(v) is not list:
        raise argparse.ArgumentTypeError(f"Argument \"{candidate}\" is not a list")
    return v


def type_conf_file(file_name: str) -> str:
    """
    Verifies that the file name has a .conf extension
    @param file_name: the file name
    @return: the name after confirming the .conf extension

    Will raise argparse.ArgumentTypeError if the file name does end
    in .conf.
    """
    if re.match(r'.*\.conf$', file_name):
        return file_name

    raise argparse.ArgumentTypeError(f"file name {file_name} does not end in .conf")


def type_input_file(file: str) -> str:
    # [file[:contractName] ...] or CONF_FILE.conf or TAC_FILE.tac

    if '.sol' in file:
        ext = 'sol'
    elif '.vy' in file:
        ext = 'vy'
    else:
        ext = None

    if ext is not None:
        '''
        Regex explanation (suppose ext=.sol):
        The file path must ends with suffix .sol: ".+\\.sol"
        A single contract name might appear. It cannot contain dots of colons:  "(:[^.:]+)?"
        '''
        if not re.search(r'^.+\.' + ext + r'(:[^.:]+)?$', file):
            raise argparse.ArgumentTypeError(f"Bad input file format of {file}. Expected <file_path>:<contract>")

        pos_file_path = Path(file).as_posix()

        if ':' in pos_file_path:
            # We split by the last occurrence of sol: in the path, which was guaranteed by te regex
            file_path_suffixless, contract = pos_file_path.rsplit("." + ext + ":", 1)
            if not re.search(r'^\w+$', contract):
                raise argparse.ArgumentTypeError(
                    f"A contract's name {contract} can contain only alphanumeric characters or underscores")
            file_path = file_path_suffixless + "." + ext
        else:
            file_path = file

        type_readable_file(file_path)
        base_name = Path(file_path).stem  # get Path's leaf name and remove the trailing ext
        if not re.search(r'^\w+$', base_name):
            raise argparse.ArgumentTypeError(
                f"file name {file} can contain only alphanumeric characters or underscores")
        return file

    elif file.endswith('.tac') or file.endswith('.conf') or file.endswith('.json'):
        type_readable_file(file)
        return file

    raise argparse.ArgumentTypeError(f"input file {file} is not in one of the supported types (.sol, .vy, .tac, .conf, "
                                     f".json)")


sanity_values = ['none', 'basic', 'advanced']


def type_rule_sanity_flag(sanity_flag: str) -> str:
    if sanity_flag in sanity_values:
        return sanity_flag
    else:
        _raise_argument_type_error(
            f'Illegal value for --rule_sanity, choose one of the following values: {sanity_values}')


def type_json_file(file: str) -> str:
    if not file.endswith('.json'):
        raise argparse.ArgumentTypeError(f"Input file {file} is not of type .json")
    type_readable_file(file)
    with open(file, 'r') as f:
        json.load(f)  # if it fails, it would throw an exception
    return file


def type_verify_arg(candidate: str) -> str:
    if not re.search(r'^\w+:[^:]+\.(spec|cvl)$', candidate):
        # Regex: name has only one ':', has at least one letter before, one letter after and ends in .spec
        raise argparse.ArgumentTypeError(f"argument {candidate} for --verify option is in incorrect form. "
                                         "Must be formatted contractName:specName.spec")
    spec_file = candidate.split(':')[1]
    type_readable_file(spec_file)

    return candidate


def type_link_arg(link: str) -> str:
    if not re.search(r'^\w+:\w+=\w+$', link):
        raise argparse.ArgumentTypeError(f"Link argument {link} must be of the form contractA:slot=contractB or "
                                         f"contractA:slot=<number>")
    return link


def type_prototype_arg(prototype: str) -> str:
    if not re.search(r'^[0-9a-fA-F]+=\w+$', prototype):
        raise argparse.ArgumentTypeError(f"Prototype argument {prototype}"
                                         f" must be of the form bytecodeString=contractName")

    return prototype


def type_struct_link(link: str) -> str:
    search_res = re.search(r'^\w+:([^:=]+)=\w+$', link)
    # We do not require firm form of slot number so we can give more informative warnings

    if search_res is None:
        raise argparse.ArgumentTypeError(f"Struct link argument {link} must be of the form contractA:<field>=contractB")
    if search_res[1].isidentifier():
        return link
    try:
        parsed_int = int(search_res[1], 0)  # an integer or a hexadecimal
        if parsed_int < 0:
            raise argparse.ArgumentTypeError(f"struct link slot number negative at {link}")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Struct link argument {link} must be of the form contractA:number=contractB"
                                         f" or contractA:fieldName=contractB")
    return link


def type_contract(contract: str) -> str:
    if not re.match(r'^\w+$', contract):
        raise argparse.ArgumentTypeError(
            f"Contract name {contract} can include only alphanumeric characters or underscores")
    return contract


def type_package(package: str) -> str:
    if not re.search("^[^=]+=[^=]+$", package):
        raise argparse.ArgumentTypeError("a package must have the form name=path")
    path = package.split('=')[1]
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"Package path {path} does not exist")
    if not os.access(path, os.R_OK):
        raise argparse.ArgumentTypeError(f"No read permissions for for packages directory {path}")
    return package


def type_settings_arg(settings: str) -> str:
    """
    Gets a string representing flags to be passed to the EVMVerifier jar via --settings,
    in the form '-a,-b=2,-c=r,q,[,..]'
    A flag can have several forms:
    1. A simple name, i.e. -foo
    2. A flag with a value, i.e. -foo=bar
    3. A flag with several values, i.e. -foo=bar,baz
    A value may be wrapped in quotes; if so, it is allowed to contain any non-quote character. For example:
    -foo="-bar,-baz=-foo" is legal
    -foo="-a",b ia also legal
    @raise argparse.ArgumentTypeError
    """
    type_logger.debug(f"settings pre-parsing= {settings}")
    settings = settings.lstrip()

    '''
    Split by commas followed by a dash UNLESS it is inside quotes. Each setting must start with a dash.
    For example:
    "-b=2, -assumeUnwindCond, -rule="bounded_supply, -m=withdrawCollateral(uint256, uint256)", -regressionTest"

    will become:
    ['-b=2',
    '-assumeUnwindCond',
    '-rule="bounded_supply, -m=withdrawCollateral(uint256, uint256)"',
    '-regressionTest']
    '''
    flags = split_by_delimiter_and_ignore_character(settings, ', -', '"', last_delimiter_chars_to_include=1)

    type_logger.debug("settings after-split= " + str(settings))
    for flag in flags:
        type_logger.debug(f"checking setting {flag}")

        if not flag.startswith("-"):
            raise argparse.ArgumentTypeError(f"illegal argument in --settings: {flag}, must start with a dash")
        if flag.startswith("--"):
            raise argparse.ArgumentTypeError(f"illegal argument in --settings: {flag} starts with -- instead of -")

        eq_split = flag.split("=", 1)
        flag_name = eq_split[0][1:]
        if len(flag_name) == 0:
            raise argparse.ArgumentTypeError(f"illegal argument in --settings: {flag} has an empty name")

        if '"' in flag_name:
            raise argparse.ArgumentTypeError(
                f'illegal argument in --settings: {flag} contained an illegal character " in the flag name')

        if len(eq_split) > 1:  # the setting was assigned one or more values
            setting_val = eq_split[1]
            if len(setting_val) == 0:
                raise argparse.ArgumentTypeError(f"illegal argument in --settings: {flag} has an empty value")

            # Values are separated by commas, unless they are inside quotes
            setting_values = split_by_delimiter_and_ignore_character(setting_val, ",", '"')
            for val in setting_values:
                val = val.strip()
                if val == "":
                    raise argparse.ArgumentTypeError(f"--setting flag {flag_name} has a missing value after comma")

                # A value can be either entirely wrapped by quotes or contain no quotes at all
                if not val.startswith('"'):
                    if '=' in val:
                        raise argparse.ArgumentTypeError(
                            f"--setting flag {flag_name} value {val} contains an illegal character =")
                    if '"' in val:
                        raise argparse.ArgumentTypeError(
                            f'--setting flag {flag_name} value {val} contains an illegal character "')
                elif not val.endswith('"'):
                    raise argparse.ArgumentTypeError(
                        f'--setting flag {flag_name} value {val} is only partially wrapped in "')

    return settings


def type_java_arg(java_args: str) -> str:
    if not re.search(r'^"[^"]+"$', java_args):  # Starts and ends with " but has no " in between them
        raise argparse.ArgumentTypeError(f'java argument must be wrapped in "", instead found {java_args}')
    return java_args


def type_address(candidate: str) -> str:
    if not re.search(r'^[^:]+:[0-9A-Fa-fxX]+$', candidate):
        # Regex: name has a single ':', has at least one character before and one alphanumeric character after
        raise argparse.ArgumentTypeError(f"Argument {candidate} of --address option is in incorrect form. "
                                         "Must be formatted <contractName>:<non-negative number>")
    return candidate

def type_solc_map(args: str) -> Dict[str, str]:
    """
    Checks that the argument is of form <sol_file_1>=<solc_1>,<sol_file_2>=<solc_2>,..
    and if all solc files are valid: they were found, and we have execution permissions for them.
    We also validate that a file doesn't have more than a single value (but that value may appear multiple times).
    Note: for backwards compatibility reasons, we also allow <contract>=<solc> syntax. We still check that no contract
    has two conflicting solc versions.

    :param args: argument of --solc_map
    :return: {Solidity_file: solc}.
             For example, if --solc_args a=solc4.25 is used, returned value will be:
             {'a': 'solc4.25'}
    :raises argparse.ArgumentTypeError if the format is wrong
    """
    args = args.replace(' ', '')  # remove whitespace

    '''
    Regex explanation:
    ([^=,]+=[^=,]+) describes a single key-value pair in the map. It must contain a single = sign, something before
    and something after.
    We allow more than one, as long as all but the last are followed by a comma hence ([^=,]+=[^=,]+,)*
    We allow nothing else inside the argument, so all is wrapped by ^ and $
    '''
    solc_matches = re.search(r'^([^=,]+=[^=,]+,)*([^=,]+=[^=,]+)$', args)

    if solc_matches is None:
        raise argparse.ArgumentTypeError(f"--solc_map argument {args} is of wrong format. Must be of format:"
                                         f"<Solidity_file>=<solc>[,..]")

    solc_map = {}  # type: Dict[str, str]
    solc_versions = set()  # If all --solc_args point to the same solc version, it is better to use --solc, and we warn
    all_warnings = set()

    for match in args.split(','):
        source_file, solc_file = match.split('=')
        is_solc_file_valid(solc_file)  # raises an exception if file is bad
        if source_file in solc_map:
            if solc_map[source_file] == solc_file:
                all_warnings.add(f"solc mapping {source_file}={solc_file} appears multiple times and is redundant")
            else:
                raise argparse.ArgumentTypeError(f"contradicting definition in --solc_map for Solidity source file "
                                                 f"{source_file}: it was given two different Solidity compilers: "
                                                 f"{solc_map[source_file]} and {solc_file}")
        else:
            solc_map[source_file] = solc_file
            solc_versions.add(solc_file)

    if len(solc_versions) == 1:
        all_warnings.add(f'All Solidity source files will be compiled with the same Solidity compiler in --solc_map. '
                         f'--solc {list(solc_versions)[0]} can be used instead')

    for warning in all_warnings:
        type_logger.warning(warning)

    type_logger.debug(f"solc_map = {solc_map}")
    return solc_map

def type_method(candidate: str) -> str:
    """
    Verifies that the given method is valid. We check for the following:
    * The format is fun_name(<primitive_types separated by commas>).
    * There are valid parenthesis
    * There are only legal characters
    * The commas appear inside the parenthesis, and separate words
    * We currently do not support complex types in methods, such as structs. We warn the user accordingly.

    This function does not check whether the primitive types exist. For example, an input foo(bar,simp) will be accepted
    even though there is no primitive type bar. This will be checked later, when we try to match the method signature
    to existing method signatures.
    :param candidate: The method input string
    :return: The same string
    :raises: ArgumentTypeError when the string is illegal (see above)
    """
    tot_opening_parenthesis_count = 0
    curr_opening_parenthesis_count = 0
    curr_str_len = 0  # length of strings that represent primitives or function names
    last_non_whitespace_char = None

    for i, char in enumerate(candidate):
        if char.isspace():
            continue
        if char == '(':
            if last_non_whitespace_char is None:
                raise argparse.ArgumentTypeError(f"malformed --method argument {candidate} - method has no name")
            elif curr_str_len == 0 and curr_opening_parenthesis_count == 0:
                raise argparse.ArgumentTypeError(
                    f"malformed --method argument {candidate} - only one pair of wrapping argument parenthesis allowed")
            tot_opening_parenthesis_count += 1
            curr_opening_parenthesis_count += 1
            curr_str_len = 0
        elif char == ')':
            curr_opening_parenthesis_count -= 1
            if curr_opening_parenthesis_count < 0:
                raise argparse.ArgumentTypeError(
                    f"malformed --method argument - too many closing parenthesis at location {i + 1} of: {candidate}")
            if last_non_whitespace_char == "," and curr_str_len == 0:
                raise argparse.ArgumentTypeError(
                    f"malformed --method argument - empty primitive type after comma at location {i + 1} of: "
                    f"{candidate}")
            if last_non_whitespace_char == "(" and curr_opening_parenthesis_count > 0:
                raise argparse.ArgumentTypeError(
                    f"malformed --method argument - empty struct at location {i - 1} of: {candidate}")
            curr_str_len = 0
        elif char == ',':
            if curr_opening_parenthesis_count == 0:
                raise argparse.ArgumentTypeError(
                    f"malformed --method argument - comma outside parenthesis at location {i + 1} of: {candidate}")
            if curr_str_len == 0 and last_non_whitespace_char != ")":
                # a comma after a struct is legal
                raise argparse.ArgumentTypeError(
                    f"malformed --method argument - empty primitive type before comma at location {i + 1} of: "
                    f"{candidate}")
            curr_str_len = 0
        elif char.isalnum() or char == '_':
            curr_str_len += 1
        elif char == "[":
            if curr_str_len < 1:
                raise argparse.ArgumentTypeError(
                    f"Bracket without a primitive type of --method argument at location {i + 1} of: {candidate}")
            if len(candidate) == i + 1 or candidate[i + 1] != "]":
                raise argparse.ArgumentTypeError(
                    f"Opening bracket not followed by a closing bracket at --method argument at location {i + 1} of: "
                    f"{candidate}")
        elif char == "]":
            if i == 0 or candidate[i - 1] != "[":
                raise argparse.ArgumentTypeError(
                    f"Closing bracket not preceded by an opening bracket at --method argument at location {i + 1} of: "
                    f"{candidate}")
        else:  # we insert spaces after commas to aid in parsing
            raise argparse.ArgumentTypeError(
                f"Unsupported character {char} in --method argument at location {i + 1} of: {candidate}")

        last_non_whitespace_char = char

    if tot_opening_parenthesis_count == 0:
        raise argparse.ArgumentTypeError(f"malformed --method argument {candidate} - no parenthesis")
    elif curr_opening_parenthesis_count > 0:
        raise argparse.ArgumentTypeError(f"malformed --method argument {candidate} - unclosed parenthesis")
    return candidate

class SplitArgsByCommas(argparse.Action):
    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: Any,
                 option_string: Optional[str] = None) -> None:
        new_values = values
        if isinstance(values, str):
            new_values = values.split(',')
        setattr(namespace, self.dest, new_values)
