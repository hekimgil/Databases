# -*- coding: utf-8 -*-
"""
@author: hekimgil

Getting external data

Code for getting external data from the Internet in various forms
and storing them in the data folder.
"""

# libraries
import os
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import shutil

import config


# settings
verbose = True
debug = True


# reload the libraries during development and debugging
if debug:
    import importlib
    importlib.reload(config)

# external data
zipurl = "https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip"
dbfile = zipurl.split('/')[-1].split('.')[0] + "_sqlite.db"

dbfolder = config.get_folders()["dbfolder"]
datfolder = config.get_folders()["datfolder"]
datfile = zipurl.split('/')[-1]
zipfolder = datfile.split('.')[0]
cc = config.get_formatting()
if os.path.isfile(os.path.join(dbfolder, dbfile)):
    if verbose:
        print(cc["CGRN"] + f"database file {dbfile} exists" + cc["CEND"])
else:
    if verbose:
        print(cc["CRED"] + f"database file {dbfile} does not exist." + cc["CEND"])
    # if os.path.isfile(os.path.join(datfolder, dbfile)):
    if os.path.isdir(os.path.join(datfolder, zipfolder)):
        if verbose:
            print(cc["CGRN"] + f"unzipped {zipfolder} folder exists" + cc["CEND"])
    else:
        if verbose:
            print(cc["CRED"] + f"unzipped {zipfolder} folder does not exist." + cc["CEND"])
            print(f"opening the {datfile}")
        with urlopen(zipurl) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                print(f"unzipping the {datfile} to a {zipfolder} folder")
                zfile.extractall(os.path.join(datfolder, zipfolder))
    print(f"copying the database file to the database folder")
    # # create the destination folder if it does not exist
    # if not os.path.exists(os.path.join(dbfolder, zipfolder)):
    #     os.makedirs(os.path.join(dbfolder, zipfolder))
    # copy the database folder
    shutil.copyfile(os.path.join(datfolder, zipfolder, zipfolder + ".db"),
                    os.path.join(dbfolder, zipfolder + "_sqlite.db"))

dbfile = os.path.join(dbfolder, zipfolder + "_sqlite.db")
print(dbfile)

if verbose:
    print("ending external...")

