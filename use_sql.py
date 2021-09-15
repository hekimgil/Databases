# -*- coding: utf-8 -*-
"""
@author: hekimgil

Getting external data

Code for getting external data from the Internet in various forms
and storing them in the data folder.
"""

# libraries
import os
import sqlite3
import pandas as pd

import external_data


# settings
verbose = True
debug = True


# reload the libraries during development and debugging
if debug:
    import importlib
    importlib.reload(external_data)


# connect to database
dbfile = external_data.dbfile
conn = sqlite3.connect(dbfile)
cur = conn.cursor()

# get a list of tables (for sqlite)
res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# table = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)
# print(table)
tables = [table[0] for table in res.fetchall()]

assert "albums" in tables
assert "artists" in tables

albums = cur.execute("SELECT * FROM albums;").fetchall()
df_albums = pd.read_sql_query("SELECT * FROM albums;", conn)
album_count = len(albums)
album_count2 = cur.execute("SELECT COUNT(*) FROM albums;").fetchone()[0]
album_count3 = cur.execute("SELECT COUNT(*) FROM albums;").fetchall()[0][0]
df_albums = pd.read_sql_query("SELECT * FROM albums;", conn)
album_count4 = df_albums.shape[0]
assert album_count == album_count2 == album_count3 == album_count4
print(f"there are {album_count} albums")

albums = cur.execute("SELECT DISTINCT(ArtistId) FROM albums;").fetchall()
album_artist_count = len(albums)
album_artist_count2 = df_albums["ArtistId"].unique().shape[0]
assert album_artist_count == album_artist_count2
print(f"there are {album_artist_count} unique artists in the albums list")

conn.close()
