#!/usr/bin/env python3

import sys
import logging
import argparse

from typing import List

import itertools
from pathlib import Path

scripts_dir_path = Path(__file__).parent.resolve()  # containing directory
sys.path.insert(0, str(scripts_dir_path))
from Shared.certoraUtils import get_certora_root_directory, COINBASE_FEATURES_MODE_CONFIG_FLAG
from Shared.certoraUtils import as_posix
from Shared.certoraUtils import get_certora_internal_dir
from Shared.certoraUtils import Mode
from types import SimpleNamespace


class CertoraContext(SimpleNamespace):
    pass


# logger for issues regarding the general run flow.
# Also serves as the default logger for errors originating from unexpected places.
run_logger = logging.getLogger("run")


def get_local_run_cmd(args: argparse.Namespace) -> str:
    """
    Assembles a jar command for local run
    @param args: A namespace including all command line input arguments
    @return: A command for running the prover locally
    """
    run_args = []
    if args.mode == Mode.TAC:
        run_args.append(args.files[0])
    if args.cache is not None:
        run_args.extend(['-cache', args.cache])
    if args.tool_output is not None:
        run_args.extend(['-json', args.tool_output])
    if args.settings is not None:
        for setting in args.settings:
            run_args.extend(setting.split('='))
    if args.coinbaseMode:
        run_args.append(COINBASE_FEATURES_MODE_CONFIG_FLAG)
    if args.skip_payable_envfree_check:
        run_args.append("-skipPayableEnvfreeCheck")
    run_args.extend(['-buildDirectory', str(get_certora_internal_dir())])
    if args.jar is not None:
        jar_path = args.jar
    else:
        certora_root_dir = as_posix(get_certora_root_directory())
        jar_path = f"{certora_root_dir}/emv.jar"

    '''
    This flag prevents the focus from being stolen from the terminal when running the java process.
    Stealing the focus makes it seem like the program is not responsive to Ctrl+C.
    Nothing wrong happens if we include this flag more than once, so we always add it.
    '''
    java_args = "-Djava.awt.headless=true"
    if args.java_args is not None:
        java_args = f"{args.java_args} {java_args}"

    return " ".join(["java", java_args, "-jar", jar_path] + run_args)


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


def __remove_parsing_whitespace(arg_list: List[str]) -> None:
    """
    Removes all whitespaces added to args by __alter_args_before_argparse():
    1. A leading space before a dash (if added)
    2. space between commas
    :param arg_list: A list of options as strings.
    """
    for idx, arg in enumerate(arg_list):
        arg_list[idx] = arg.strip().replace(', ', ',')
