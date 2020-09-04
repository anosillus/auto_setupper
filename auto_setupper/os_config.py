#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: os_config.py
# First Edit: 2020-09-02
# Last Change: 04-Sep-2020.
"""
This scrip is for test

"""
import itertools
import platform
from pathlib import Path
from typing import Dict, List


class OS_Info:
    os_name: str
    option_dict: Dict
    readable_exts: List[str]
    positive_list: List[str]
    negative_list: List[str]

    def get_os_negaposi_dict(self):
        return {"positive": self.positive_list, "negtive": self.negative_list}


def get_my_os_info():
    if is_windows():
        return Windows()
    elif is_debian():
        return Debian()
    elif is_darwin():
        return Darwin()


def Windows():
    Windows = OS_Info()
    Windows.os_name = "Windows"
    Windows.option_dict = {
        "": "chocolatey install",
        "S": "scoope install",
        "W": False,  # Microsoft_App
        "wsl": False,  # WSL
        "M": False,  # Install-module
    }
    Windows.readable_exts = [".cmd", ".ps1"]
    Windows.positive_list = [".msi", "exe", "win64", "win32", ".zip", "7z"]
    Windows.negative_list = ["pdb"]

    return Windows


def Darwin():
    Darwin = OS_Info()
    Darwin.os_name = "Darwin"
    Darwin.option_dict = {
        "": "brew install",
        "C": "brew cask install",
        "M": "Mas install",
    }
    Darwin.readable_exts = ["darwin.sh", ".sh"]
    Darwin.positive_list = [".app", ".pkg", ".dmp", ".zip", ".7z"]
    Darwin.negative_list = ["linux", "windows"]

    return Darwin


def Debian():
    Debian = OS_Info()
    Debian.os_name = "Debian"
    Debian.option_dict = {"": "sudo apt-get install", "S": "sudo snap install"}
    Debian.readable_exts = ["debian.sh", ".sh"]
    Debian.positive_list = [".deb", "debian" "linux", "arm64", ".zip", ".7z"]
    Debian.negative_list = ["pdb"]

    return Debian


def is_os(os_name):
    return platform.system() == os_name


def is_windows():
    return is_os("Windows")


def is_debian():
    return is_os("Linux")


def is_darwin():
    return is_os("Darwin")
