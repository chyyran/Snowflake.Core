__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import re


class Command():

    def __init__(self, command, params=[]):
        self.command = command
        self.params = params

    @classmethod
    def command_from_dict(cls, dict):
        command = Command(dict["command"], dict["params"])
        return command