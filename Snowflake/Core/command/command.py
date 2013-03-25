#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import Snowflake.Core.snowflakeutils as Utils
import Snowflake.Core.scrape_engines.deep_engine as engine

class Command():
    def __init__(self, command, params={}):
        self.command = command
        self.params = params

    @classmethod
    def command_from_dict(cls, dict):
        command = Command(dict["command"], dict["params"])
        return command

    @staticmethod
    def get_cmd_format(cls):
        return
    def __repr__(self):
        CommandExecutor.run_command(self)


class CommandExecutor():
    @staticmethod
    def run_command(cmd):
        if cmd.command == CommandDefinitions.SCRAPE_GAMES:
            return CommandExecutor.scrape_games(cmd.params)

    @staticmethod
    def scrape_games(params):
        if params["gamename"] is None:
            return None
        else:
            return engine.scrape_game(params["gamename"],params["console"],
                               Utils.ConfigUtils.get_console_from_config(params["console"]).scrapers)


class CommandDefinitions():
    class __metaclass__(type):
        def __iter__(self):
            for key in CommandDefinitions.__dict__:
                if not key.startswith("__"):
                    yield CommandDefinitions.__dict__[key]

    SCRAPE_GAMES = "ScrapeGames"

