#coding=utf-8

from snowflake.utils import generalutils, configutils
from snowflake.scrape_engines import deep_engine as engine

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


@rpcmethod("ScrapeGame")
def scrape_game(gamename, console):
    """
    RPC Method to scrape a game by gamename and console
    :param gamename:
    :param console:
    :return:
    """
    generalutils.server_log("ScrapeGames Requested  - gamename = {0} console = {1}".format(gamename,console))
    if gamename is None:
        return None
    else:
        return engine.scrape_game(gamename, console,
                                  configutils.get_console_from_config(console).scrapers)

@rpcmethod("GetConsoles")
def get_consoles():
    """
    RPCMethod gets consoles from configuration

    :return:
    """
    generalutils.server_log("GetConsoles Requested")
    consoles = []
    for console in configutils.get_all_consoles():
        consoles.append(console.__dict__)
    return consoles

