#coding=utf-8
from Snowflake.Core.command.command import CommandDefinitions
from Snowflake.Core.scrape_engines import deep_engine as engine
import json
from Snowflake.Core.utils.configutils import ConfigUtils

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

def run_command(cmd):
    if cmd.command == CommandDefinitions.SCRAPE_GAMES:
        return scrape_games(cmd.params)


def scrape_games(params):
    if params["gamename"] is None:
        return None
    else:
        return engine.scrape_game(params["gamename"],params["console"],
                               ConfigUtils.get_console_from_config(params["console"]).scrapers)


def get_consoles():
    consoles = []
    for console in ConfigUtils.get_all_consoles():
        consoles.append(console.__dict__)
    return consoles

