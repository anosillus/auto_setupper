#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: github.py
# First Edit: 2020-09-01
# Last Change: 04-Sep-2020.
"""
This scrip is for test

"""
from typing import Dict, List
from auto_setupper import github


def test_is_github_api():
    assert not github.is_github_api("http://example.com")
    assert github.is_github_api(
        "https://api.github.com/repos/git-for-windows/git/releases"
    )
    assert not github.is_github_api(
        "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US"
    )


def test_get_body_data():
    assert isinstance(
        github.get_body_data(
            "https://api.github.com/repos/git-for-windows/git/releases"
        ),
        list,
    )
    assert isinstance(
        github.get_body_data(
            "https://api.github.com/repos/git-for-windows/git/releases"
        )[0],
        dict,
    )


def test_find_download_urls():
    assert (
        len(
            github.find_download_urls(
                github.get_body_data(
                    "https://api.github.com/repos/git-for-windows/git/releases"
                )
            )
        )
        > 2
    )
    assert (
        len(
            github.find_download_urls(
                github.get_body_data(
                    "https://api.github.com/repos/git-for-windows/git/releases"
                )
            )
        )
        < 400
    )


def test_is_url_exist():
    pass


def get_download_link_from_github():
    pass


def test_grep_release_files_with_negaposi_word():
    file_urls = [
        "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-64-bit.exe",
        "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-32-bit.exe",
        "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/PortableGit-2.28.0-64-bit.7z.exe",
        "https://github.com/git-for-windows/git/releases/download/v2.25.0-rc1.windows.1/PortableGit-2.25.0.rc1.windows.1-64-bit.7z.exe",
    ]
    readable_exts = [".exe"]
    negaposi_dict = {"positive": ["win64"], "negative": ["Portable"]}

    assert (
        "https://github.com/git-for-windows/git/releases/download/v2.28.0.windows.1/Git-2.28.0-64-bit.exe"
        == github.find_suitable_github_release(
            file_urls, negaposi_dict, readable_exts
        )
    )


def test_find_suitable_github_release():
    pass


def test_is_one_candidate():
    pass


def test_get_file_names_dict():
    pass


def test_merge_negaposi_dict():
    pass
