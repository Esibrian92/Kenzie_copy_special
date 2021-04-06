#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Erick Sibrian"

import re
import os
import sys
import shutil
import subprocess
import argparse

cwd = os.getcwd()
# print("current working directory:", cwd)
# file_list = os.walk(os.getcwd())
# print("this are the files:", file_list)
# pattern = r"[__w__]"
# for items in file_list:
#     if pattern in items:
#         print(items)


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    dir_list = os.listdir(dirname)
    name = r"[\w+[__w__]\w+]"
    print(dir_list)
    # matches = re.findall(name, dir_list)
    for file_name in dir_list:
        print(file_name)


def copy_to(path_list, dest_dir):
    # your code here
    return


def zip_to(path_list, dest_zip):
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser(
        description="read,copy,and move directories")
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='files from directory')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    if not ns:
        parser.print_usage()
        sys.exit(1)

    dir_list = ns.from_dir

    # Your code here: Invoke (call) your functions
    get_special_paths(dir_list)


if __name__ == "__main__":
    main(sys.argv[1:])
