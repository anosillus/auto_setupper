# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: command.py
# First Edit: 2020-09-01
# Last Change: 04-Sep-2020.
"""
This scrip is for test

"""
import itertools
import subprocess
from pathlib import Path


def run_in_terminal(command):
    proc = subprocess.Popen(command)
    try:
        _, _ = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        print(outs, errs)


def get_command(data, os_option_dict):
    install_option, name = option_checker(data)

    return str(os_option_dict.get(install_option)) + name


def option_checker(data):
    if len(data.split(":") == 1):
        return "", data
    else:
        return data.split(":")[0], data.split(":")[1:]


def get_script(script_file_stem, script_dir, exts):
    files = Path("./script").glob(script_file_stem)

    if len(files) and len(exts):
        for ext, file in itertools.product(exts, files):
            if ext in str(file):
                # I should add cmd/ps1 run command option herer.

                return ". " + str(file)
    else:
        print(script_file_stem, exts)
        raise "Error at finding script file"
