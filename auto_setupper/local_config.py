# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: local_config.py
# First Edit: 2020-09-01
# Last Change: 03-Sep-2020.
"""
This scrip is for test

"""
import itertools
import re
from pathlib import Path
from typing import List


def get_csv_file_path(file_path: str = ""):
    """
    get_csv_file_path is return csv_file path as posix style.
    Default is './app.csv', but you can enter any file path.

    :param file_path: '/User/home/test.csv'
    :type file_path: str
    """

    if file_path:
        return str(Path(file_path).as_posix())
    else:
        return str(Path(Path.cwd() / Path("app.csv")).as_posix())


def get_negaposi_rule_dict(row_data):
    return {
        "positive": [
            data.strip() for data in row_data.get("positive_rule").split(",")
        ]
        if row_data.get("positive_rule")
        else [],
        "negative": [
            data.strip() for data in row_data.get("negative_rule").split(",")
        ]
        if row_data.get("negative_rule")
        else [],
    }


def get_file_name_from_url(file_url):
    return re.sub(r'[\\/:*?"<>|]+', "", file_url.split("/")[-1])


def make_downloaded_path(file_name, download_directory):
    return str(Path(download_directory) / Path(file_name).as_posix())
