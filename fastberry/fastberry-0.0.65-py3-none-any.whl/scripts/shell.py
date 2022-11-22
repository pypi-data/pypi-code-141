"""
    Shell Functions
"""

import os
import pathlib
import shlex
import shutil
import subprocess
import zipfile

import click

TEMPORARY_DIR = pathlib.Path(__file__).parents[0] / "tmp"


def shell_commands(list_of_commands):
    """Shell Commands"""
    processes = []
    for cmd in list_of_commands:
        __code = shlex.split(cmd)
        task = subprocess.Popen(__code, shell=True)
        processes.append(task)
    return [process.wait() for process in processes]


def shell_print(text: str, color: str = "green"):
    """Shell Print"""
    return click.secho(f"{ text }", fg=color, bold=True)


def unzip_base(source, destination):
    """Unzip Base"""
    with zipfile.ZipFile(source, "r") as zip_ref:
        zip_ref.extractall(destination)


def unzip(source: pathlib.Path, destination: pathlib.Path):
    """Unzip Method"""
    zipfile_name = source.name.replace(".zip", "")
    unzip_base(source, TEMPORARY_DIR)
    tmp = TEMPORARY_DIR / zipfile_name
    file_names = os.listdir(tmp)
    for file_name in file_names:
        try:
            shutil.move(os.path.join(tmp, file_name), destination)
        except:
            pass
    shutil.rmtree(tmp, ignore_errors=False, onerror=None)
