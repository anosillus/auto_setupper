#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: test.py
# First Edit: 2020-09-01
# Last Change: 04-Sep-2020.
"""
This scrip is for test

"""
import csv
import json
from pathlib import Path
from pprint import pprint

# import main
import file_reader
import github
import local_config


def test_get_csv_file_path():
    assert local_config.get_csv_file_path() == str(
        Path(
            "C:\\Users\\anosillus\\dev\\auto_install\\auto_install\\app.csv"
        ).as_posix()
    )
    assert local_config.get_csv_file_path("./mini_app.csv") == str(
        Path(".\\mini_app.csv").as_posix()
    )


def test_find_suitable_github_release():
    file_urls = [
        "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-64-bit.exe",
        "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-32-bit.exe",
        "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/PortableGit-2.28.0-64-bit.7z.exe",
        "https://github.com/git-for-windows/git/releases/download/v2.25.0-rc1.windows.1/PortableGit-2.25.0.rc1.windows.1-64-bit.7z.exe",
    ]
    readable_exts = [".exe"]
    positive_words = ["win64"]
    negative_words = ["Portable"]
    assert (
        "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-64-bit.exe"
        == github.find_suitable_github_release(
            file_urls, readable_exts, positive_words, negative_words
        )
    )


def test_get_file_names_dict():
    url = "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-64-bit.exe"
    assert {"Git-2.28.0-64-bit.exe": url} == github.get_file_names_dict([url])


def test_get_file_nam_from_url():
    assert (
        "product=firefox-latest-ssl&os=win64&lang=en-US"
        == local_config.get_file_name_from_url(
            "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"
        )
    )


def test_make_downloaded_path():
    file_name = "test_file.txt"
    download_directory = str(Path().home())
    assert (
        "C:\\Users\\anosillus\\test_file.txt"
        == local_config.make_downloaded_path(file_name, download_directory)
    )


def test_get_negaposi_rule_dict():
    d = {"positive_rule": None, "negative_rule": None}
    assert {
        "positive": [],
        "negative": [],
    } == local_config.get_negaposi_rule_dict(d)
    d2 = {"positive_rule": "happy, party", "negative_rule": "sad"}
    assert {
        "positive": ["happy", "party"],
        "negative": ["sad"],
    } == local_config.get_negaposi_rule_dict(d2)
