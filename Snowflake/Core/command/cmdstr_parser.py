#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import re
from command import Command, CommandDefinitions


def parse(input):
    input = input.replace("\"", "").replace("\'", "").strip()
    command = re.findall(r"(?<=!).*?(?=:)", input)[0]
    if command not in CommandDefinitions:
        return "Invalid Command"
    params = re.findall(r"(?<=:).*", input)[0].split(",")
    paramdict = {}
    for param in params:
        paramdict[param.split("=")[0]] = param.split("=")[1]
    command_dict = {"command": command, "params": paramdict}
    return Command.command_from_dict(command_dict)