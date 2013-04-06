#coding=utf-8
import re
from Snowflake.Core.command import cmdstr_parser

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


class CommandUtils:

    @staticmethod
    def get_cmd_format(input):
        fmt = re.match(r"^.*?(?=\!)",input).group(0)
        return fmt

    @staticmethod
    def process_cmd(cmd):
        if CommandUtils.get_cmd_format(cmd) != "cmdstr":
            return "Unknown Format"
        else:
            command = cmdstr_parser.parse(cmd)
            return command