# -*- coding: utf-8 -*-
"""
@author: hekimgil

Configuration file

This file contains the common configuration code.
"""

# libraries
import os


def get_folders():
    # check to see if the directory name matches the original design
    assert os.getcwd()[-9:] == "Databases"

    # folder locations
    basfolder = os.getcwd()
    folders = {
        "datfolder": os.path.join(basfolder, "data", ""),
        "dbfolder": os.path.join(basfolder, "db", "")
    }
    return folders


def get_formatting():
    # color codes for the console output
    ccodes = {
        "CGRN": "\033[1;32m",
        "CRED": "\033[1;31m",
        "CYEL": "\033[1;33m",
        "CCYN": "\033[1;36m",
        "CEND": "\033[0m",

        "CMGN": "\033[1;35m",
        "CBLU": "\033[1;34m",
        "CGRNBND": "\033[1;42m",
        "CBLUBND": "\033[1;44m",
        "CMGNBND": "\033[1;45m"
    }
    return ccodes
