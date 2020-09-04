# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: file_reader.py
# First Edit: 2020-09-01
# Last Change: 04-Sep-2020.
"""
This scrip is for test

"""

import csv
import re
from pathlib import Path
from typing import Dict, List


def read_csv(csv_file_path: str):
    """
    read_csv
    Open and read the file and return CsvReader class.

    :param csv_file_path:
    :type file_path: str
    """

    return csv.DictReader(open(str(Path(csv_file_path).as_posix())))


def option_checker(content: str) -> List:
    """
    option_checker.
    Get target file name and install-option from content.

    :param data:
    :type os_name: str

    :rtype: List[str, str]
    :[insatll_option:str, target_name:str] like ['s', 'chrome']
    """

    if ":" in content:
        return content.split(":", 1)
    else:
        return ["", content]


def is_url(data: str) -> bool:
    """is_url.

    :param data:
    :type data: str
    :rtype: bool
    """

    return re.match("^(?:http|ftp)s?://", data)


def get_main_content_from_csv(row_data: Dict, os_name: str) -> str:
    """
    get_main_content_from_csv.
    Select target content by considering os_type from csv_data.

    :param row_data:
    :type row_data: Dict
    :param os_name:
    :type os_name: str

    :rtype: str
    target-content like "s:git", "https://github.com/~~/ruby.deb"
    """

    if (not row_data.get(os_name)) or (row_data.get(os_name) == "?"):
        return ""
    else:
        return row_data.get(os_name).rstrip()
