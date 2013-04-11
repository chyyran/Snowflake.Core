#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import sqlite3
import os
import Snowflake.Core.utils.generalutils as generalutils

def create_games_database():
    #CREATE TABLE games (id INTEGER PRIMARY KEY, game_name TEXT, description TEXT, release_year TEXT, rom_path TEXT, publisher TEXT, cover_url TEXT, console_name TEXT, fanart_url TEXT, fanart_path TEXT, cover_path TEXT);
    try:
        dbpath = os.path.join(generalutils.get_core_directory(), "assets", "games.db")
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute("CREATE TABLE games (\
                    id INTEGER PRIMARY KEY,\
                    game_name TEXT,\
                    description TEXT,\
                    release_year TEXT, \
                    rom_path TEXT, \
                    publisher TEXT, \
                    cover_url TEXT, \
                    console_name TEXT, \
                    fanart_url TEXT, \
                    fanart_path TEXT, \
                    cover_path TEXT)")
        con.commit()
        return True
    except sqlite3.Error, e:
        generalutils.server_log("Failed to create games database: " + e.args[0])
        return False


def insert_game(game):
    try:
        dbpath = os.path.join(generalutils.get_core_directory(), "assets", "games.db")
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute('INSERT INTO games VALUES(\
                    NULL,\
                    "{game_name}",\
                    "{description}",\
                    "{release_year}",\
                    "{rom_path}",\
                    "{publisher}",\
                    "{cover_url}",\
                    "{console_name}",\
                    "{fanart_url}",\
                    "{fanart_path}",\
                    "{cover_path}")'.format(**game.__dict__).replace('\'', '\'\''))
        con.commit()
        return True
    except sqlite3.Error, e:
        generalutils.server_log("Failed to insert game: " + e.args[0])
        return False