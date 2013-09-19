#coding=utf-8
from snowflake import config, utils, database

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


def rpcmethod(rpcname):
    """
    Add this decorator with the RPC method name to all RPC methods
    :param rpcname:
    :return:
    """

    def deco(func):
        setattr(func, "__rpcname__", rpcname)
        return func
    return deco


#@rpcmethod("ScrapeGame")
#def scrape_game(gamename, console):
#    """
#    RPC Method to scrape a game by gamename and console
#    :param gamename:
#    :param console:
#    :return:
#    """
#    generalutils.server_log("ScrapeGames Requested  - gamename = {0} console = {1}".format(gamename,console))
#    if gamename is None:
#        return None
#    else:
#        return engine.scrape_game(gamename, console,
#                                  data.get_console_from_config(console).scrapers)

@rpcmethod("GetConsoles")
def get_consoles():
    """
    RPCMethod gets consoles from configuration

    :return:
    """
    utils.server_log("GetConsoles Requested")
    return config.get_consoles()

@rpcmethod("GetGameByID")
def get_game_by_id(game_id):
    utils.server_log("GetGameByID Requested. Params={0}".format(game_id))
    #todo test this
    return database.get_game_by_uid(game_id)

@rpcmethod("SearchGame")
def search_game(name="", systemid="", metadata={}):
    #todo test this
    return database.search_game(name, systemid, metadata)

@rpcmethod("GetGamesForSystem")
def get_games_for_system(systemid):
    return database.get_games_for_system(systemid)