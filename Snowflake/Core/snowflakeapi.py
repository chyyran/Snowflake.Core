#coding=utf-8

from Snowflake.Core.scrape_engines import deep_engine as engine
import json
import Snowflake.Core.utils.configutils as configutils
from Snowflake.Core.utils.generalutils import rpc_func
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

#def run_command(cmd):
#    if cmd.command == CommandDefinitions.SCRAPE_GAMES:
#        return scrape_games(cmd.params)


def scrape_games(gamename, console):
    __rpcname__ = "ScrapeGames"
    if gamename is None:
        return None
    else:
        return engine.scrape_game(gamename,console,
                               configutils.get_console_from_config(console).scrapers)


def get_consoles():
    __rpcname__= "GetConsoles"
    consoles = []
    for console in configutils.get_all_consoles():
        consoles.append(console.__dict__)
    return consoles

