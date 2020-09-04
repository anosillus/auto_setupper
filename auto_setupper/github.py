#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: github.py
# First Edit: 2020-09-01
# Last Change: 04-Sep-2020.
"""
This scrip is for test

"""
import itertools
import json
import urllib
import urllib.error
import urllib.request
from typing import Dict, List
import my_error


def is_github_api(url) -> bool:
    return "https://api.github.com/repos/" in url


def get_body_data(github_url):
    try:
        with urllib.request.urlopen(github_url) as response:
            return json.loads(response.read())
            # headers = response.getheaders()
            # status = response.getcode()

    except urllib.error.URLError as e:
        print(e.reason)


def find_download_urls(release_page_body):
    """
    find_download_urls is parse and grep tarfind_urls.

    :param release_page_body:
    """
    file_urls = []

    if isinstance(release_page_body, list):
        for paresr in release_page_body:
            file_urls.extend(find_download_urls(paresr))
    elif isinstance(release_page_body, dict):
        if release_page_body.get("browser_download_url"):
            file_urls.append(release_page_body.get("browser_download_url"))
        else:
            for value in release_page_body.values():
                file_urls.extend(find_download_urls(value))

    return file_urls


def is_url_exist(urls: List):
    if not urls:
        my_error.url_does_not_exist()


def get_download_link_from_github(
    github_url, os_negapoi_dict, user_negaposi_dict, readable_exts
):
    file_urls = find_download_urls(get_body_data(github_url))
    is_url_exist(file_urls)

    if len(file_urls) == 1:
        return file_urls[0]

    merged_negaposi_dict = merge_negaposi_dict(
        os_negapoi_dict, user_negaposi_dict  #
    )

    return find_suitable_github_release(
        file_urls, merged_negaposi_dict, readable_exts
    )


def grep_release_files_with_negaposi_word(
    possible_files_dict: Dict, word: str, positive: bool
):
    """
    grep_release_files_with_negaposi_word.

    :param possible_files: {hoge_win64.exe:http~/hoge_win64.exe, hoge_win32.exe:~, hoge.deb:~}
    :type possible_files: Dict[str:str]
    :param word: 'win64'
    :type word: str
    :param positive: True
    :type positive: bool

    return  {hoge_win64.exe:http~/hoge_win64.exe}
    """

    if word:
        # longest_zip return ("positive", "None"). Stop grepping with None.

        if positive:
            # When positive case, confirm the word exists in file_name.
            greped_files_dict = {
                file_name: file_url
                for file_name, file_url in possible_files_dict.items()
                if word in file_name
            }
        else:
            # When negative case, confirm the word doesn't exists in file_name.
            greped_files_dict = {
                file_name: file_url
                for file_name, file_url in possible_files_dict.items()
                if word not in file_name
            }

        if greped_files_dict:
            return greped_files_dict

    return possible_files_dict


def find_suitable_github_release(
    file_urls, merged_negaposi_dict, readable_exts
):

    file_names_dict = get_file_names_dict(file_urls)

    # print(merged_negaposi_dict)

    for positive_word, negative_word in itertools.zip_longest(
        merged_negaposi_dict.get("positive"),
        merged_negaposi_dict.get("negative"),
    ):
        if is_one_candidate(file_names_dict):
            break

        file_names_dict = grep_release_files_with_negaposi_word(
            file_names_dict, positive_word, positive=True
        )

        file_names_dict = grep_release_files_with_negaposi_word(
            file_names_dict, negative_word, positive=False
        )

    return list(file_names_dict.values())[0]


def is_one_candidate(file_names_dict):
    return len(file_names_dict) == 1


def get_file_names_dict(file_urls):
    return {file_url.split("/")[-1]: file_url for file_url in file_urls}


def check_is_none(data):
    if data:
        print(data, 1)

        return data
    else:
        print(data, 2)

        return []


def merge_negaposi_dict(os_negapoi_dict, user_negaposi_dict):
    p = "positive"
    n = "negative"
    # b = check_is_none(os_negapoi_dict.get(p))
    # print(b)
    return {
        p: check_is_none(os_negapoi_dict.get(p)).extend(
            check_is_none(user_negaposi_dict.get(p))
        ),
        n: check_is_none(os_negapoi_dict.get(n)).append(
            check_is_none(user_negaposi_dict.get(n))
        ),
    }
