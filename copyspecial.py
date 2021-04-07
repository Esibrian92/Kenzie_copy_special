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


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    dir_list = os.listdir(dirname)
    pattern = r"__\w+__"
    file_list = []
    for filename in dir_list:
        match = re.search(pattern, filename)
        if match:
            file_list.append(os.path.abspath(os.path.join(dirname, filename)))
    return file_list


def copy_to(path_list, dest_dir):
    """checks to see if a directory exist, looks through it and copies the files
     to a new given destination if it exist.if not it makes a given
     destination"""
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)


def zip_to(path_list, dest_zip):
    """zips the files to a new destination"""
    cmd = ["zip", "-j", dest_zip]
    cmd.extend(path_list)
    subprocess.check_output(cmd)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser(
        description="read,copy,and move directories")
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    """adds a new argument to the args.parse, so the from_dir command can be used
     in the command line"""
    parser.add_argument('from_dir', help='files from directory')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    """prints out the usage and exits the program with and exit code of 1 if ns
     is untrue in anyway (errors)"""
    if not ns:
        parser.print_usage()
        sys.exit(1)

    # Your code here: Invoke (call) your functions
    """by setting the funtion equal to a variable now we can use it as an object
     and see everything it conatains"""
    special_paths = get_special_paths(ns.from_dir)

    """conditions in wich to run the functions from above"""

    if ns.todir:
        copy_to(special_paths, ns.todir)

    elif ns.tozip:
        message = "I am going to : "
        print(message)
        zip_to(special_paths, ns.tozip)
    else:
        for path in special_paths:
            print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
