#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import sqlite3
import os
import json
import Snowflake.Core.utils.generalutils as generalutils

def create_games_database():
    """

    Creates games database if not there
    :return:
    """
    try:
        dbpath = os.path.join(generalutils.get_core_directory(), "assets", "games.db")
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute("CREATE TABLE games (\
                    id TEXT,\
                    gamename TEXT,\
                    systemid TEXT,\
                    rompath TEXT,\
                    mediapath TEXT,\
                    metadata TEXT")
        con.commit()
        return True
    except sqlite3.Error, e:
        generalutils.server_log("Failed to create games database: " + e.args[0])
        return False


def insert_game(game):

    """
    Adds a game to the database
    :param game:
    :return:
    """
    try:
        dbpath = os.path.join(generalutils.get_core_directory(), "assets", "games.db")
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute('INSERT INTO games VALUES({uuid},{game_name},{system_id},{rom_path},{media_path},'
                    .format(**game.__dict__).replace('\'', '\'\'') + json.dumps(game.metadata) + ")")
        con.commit()
        return True
    except sqlite3.Error, e:
        generalutils.server_log("Failed to insert game: " + e.args[0])
        return False

def delete_game_by_id(gameid):
    pass


def delete_game_by_game(gameobj):
    pass


def get_game_by_name(name,system):
    pass


def get_game_by_uid(id):
    pass


def get_games_from_system(system):
    pass


def delete_system(system):
    pass
