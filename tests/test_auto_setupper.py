# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# File name: main.py
# First Edit: 2020-09-01
# Last Change: 04-Sep-2020.
"""
Main module.
"""
# from typing import Dict, List

from command import get_command, get_script, option_checker, run_in_terminal
from download import download
from file_reader import get_main_content_from_csv, is_url, read_csv
from github import get_download_link_from_github, is_github_api
from local_config import (get_csv_file_path, get_file_name_from_url,
                          get_negaposi_rule_dict, make_downloaded_path)
from os_config import get_my_os_info

SCRIPT_DIR = "./../assets/download_script"
DOWNLOAD_DIR = "./../assets/test_download/"
CSV_PATH = "./../assets/csv_file/mini_app.csv"


def main():
    MyOS = get_my_os_info()
    CsvFileReader = read_csv(get_csv_file_path(CSV_PATH))

    for row_data in CsvFileReader:
        # if condition_checker(row_data, ignore_rules): # NotImplemented
        #    continue
        # Grep with condition like kind of Tools, like CUI tool only.

        if content := get_main_content_from_csv(row_data, MyOS):
            print(row_data)
            print(MyOS.os_name)

            continue
        elif is_url(content):
            if is_github_api(get_main_content_from_csv(content, MyOS)):
                download_link = get_download_link_from_github(
                    content,
                    MyOS,
                    get_negaposi_rule_dict(row_data),
                )
            else:
                download_link = content
            download(
                download_link,
                make_downloaded_path(
                    get_file_name_from_url(download_link), DOWNLOAD_DIR
                ),
            )
        else:
            install_option, name = option_checker(content)

            if install_option == "s":
                run_in_terminal(
                    get_script(name, SCRIPT_DIR, MyOS.readable_exts)
                )
            else:
                run_in_terminal(get_command(content, MyOS.option_dict))


if __name__ == "__main__":
    main()
