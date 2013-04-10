#coding=utf-8

from Snowflake.Core.scrape_engines import deep_engine as engine
import json
import Snowflake.Core.utils.configutils as configutils
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


def rpcmethod(rpcname):
    def deco(func):
        setattr(func, "__rpcname__", rpcname)
        return func
    return deco


@rpcmethod("ScrapeGame")
def scrape_game(gamename, console):
    if gamename is None:
        return None
    else:
        return engine.scrape_game(gamename,console,
                configutils.get_console_from_config(console).scrapers)

@rpcmethod("GetConsoles")
def get_consoles():
    consoles = []
    for console in configutils.get_all_consoles():
        consoles.append(console.__dict__)
    return consoles

