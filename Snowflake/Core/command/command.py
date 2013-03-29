#coding=utf-8

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import re

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
        fmt = re.match(r"^.*?(?=\!)",input).group(0)
        return fmt

    def __repr__(self):
        return self.__dict__



class CommandDefinitions():
    class __metaclass__(type):
        def __iter__(self):
            for key in CommandDefinitions.__dict__:
                if not key.startswith("__"):
                    yield CommandDefinitions.__dict__[key]

    SCRAPE_GAMES = "ScrapeGames"


