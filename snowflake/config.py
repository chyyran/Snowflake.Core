#coding=utf-8
import os
import yaml

from snowflake import utils, constants
from snowflake.types import System

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


def get_config():
    return yaml.load(open(os.path.join(constants.directory_core, "data.yml")))


def get_console_by_id(id):
    for system in yaml.load(open(os.path.join(constants.directory_core, "systems.yml"))):
        if id == system["id"]:
            return System(**system)
    return None


def get_all_consoles():
    consoles = []
    for system in yaml.load(open(os.path.join(constants.directory_core, "systems.yml"))):

        consoles.append(get_console_by_id(system["id"]))
    return consoles
