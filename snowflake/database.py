#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.snowflake
"""
import sqlite3
import os
import json
from snowflake.utils import generalutils
from snowflake.datastructures import Game
#Games Database
games_db = sqlite3.connect(os.path.join(generalutils.get_core_directory(), "assets", "games.db"))


def create_games_database():
    """
    Creates games database if not there
    :return:
    """
    try:
        games_db.cursor().execute("CREATE TABLE games "
                                  "(uuid TEXT, gamename TEXT, systemid TEXT, rompath TEXT, mediapath TEXT, metadata TEXT)")
        games_db.commit()
        return True
    except sqlite3.Error, e:
        generalutils.server_log("SQL Error Encountered, Unable to Create Database:", e.args[0])
        return False


def insert_game(game):
    """
    Adds a game to the database
    :param game:
    :return:
    """

    try:
        #Because we don't know how much metadata there will be, we use ''.join() for efficiency
        games_db.cursor().execute(''.join([
            'INSERT INTO games VALUES("{uuid}","{gamename}","{systemid}","{rompath}","{mediapath}","'
            .format(**game.__dict__).replace("'", "''"),
            json.dumps(game.metadata).replace('"', '""'), '")'
        ]))

        games_db.commit()
        generalutils.server_log("Inserted Game '{gamename}' ({rompath}) with uuid {uuid}".format(**game.__dict__))
        return True
    except sqlite3.Error, e:
        generalutils.server_log("SQL Error Encountered, Unable to Insert Game:", e.args[0])
        return False

def delete_game_by_id(gameid):
    pass


def delete_game_by_game(gameobj):
    pass


def get_game_by_name(name, system):
    pass


def get_game_by_uid(id):
    pass


def get_games_from_system(system):
    games = []
    try:
        cur = games_db.cursor()
        cur.execute('SELECT * FROM games WHERE systemid="{0}"'.format(system))

        #todo Test this. Too tired tonight :/
        for result in cur.fetchall():
            uuid, gamename, systemid, rompath, mediapath, metadata = result
            games.append(Game(uuid, gamename, systemid, rompath, mediapath, **json.loads(metadata)))

    except sqlite3.Error, e:
        generalutils.server_log("SQL Error Encountered, Could not search for games")

    return games

def delete_system(system):
    pass
