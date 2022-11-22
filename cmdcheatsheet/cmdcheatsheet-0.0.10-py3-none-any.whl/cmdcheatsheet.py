#!/bin/python3
import sys

from cmdcheatsheet.logger import error
from cmdcheatsheet.command_list import get_command_by_name
from cmdcheatsheet.config import setup_app


def main():
    setup_app()

    if len(sys.argv) == 1:
        sys.argv.append('-p')

    command = sys.argv[1]
    args = sys.argv[2:]

    try:
        command_to_invoke = get_command_by_name(command)
        if command_to_invoke:
            command_to_invoke.handle(args)
        else:
            error("Please provide the valid command name.")

    except Exception as e:
        error(e)

if __name__ == '__main__':
    main()
