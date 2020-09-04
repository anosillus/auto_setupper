# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: file_reader.py
# First Edit: 2020-09-01
# Last Change: 04-Sep-2020.
"""
This scrip is for test

"""

from auto_setupper import file_reader


def test_read_csv(csv_path="./../assets/csv_file/mini_app.csv"):
    data_reader = file_reader.read_csv(csv_path)
    assert next(data_reader) == {
        "name": "git",
        "category": "D-tool",
        "UI": "Both",
        "speed": "2",
        "dev": "?",
        "joy": "",
        "Windows": "https://api.github.com/repos/git-for-windows/git/releases",
        "Darwin": "git",
        "Debian": "git",
        "windows_message": "",
        "darwin_message": "",
        "debian_mssage": "",
        "positive_rule": "",
        "negative_rule": "mingit, portable",
        "citation": "",
        "location": "",
        "config_file": "",
    }


def test_option_checker():
    assert ["", "git"] == file_reader.option_checker("git")
    assert ["s", "code"] == file_reader.option_checker("s:code")


def test_is_url():
    assert not file_reader.is_url("megaman.exe")
    assert file_reader.is_url("https://example.com")
    assert not file_reader.is_url("example.com")


def test_get_main_content_from_csv():
    row = {
        "Windows": "https://api.github.com/repos/git-for-windows/git/releases",
        "Darwin": "git",
        "Debian": "git",
    }

    assert (
        "https://api.github.com/repos/git-for-windows/git/releases"
        == file_reader.get_main_content_from_csv(row, "Windows")
    )
    assert "git" == file_reader.get_main_content_from_csv(row, "Debian")
