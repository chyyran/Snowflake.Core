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


def get_system_by_id(systemid):
    for system in yaml.load(open(os.path.join(constants.directory_core, "systems.yml"))):
        if systemid == system["id"]:
            return System(**system)
    return None


def get_all_systems():
    systems = []
    for system in yaml.load(open(os.path.join(constants.directory_core, "systems.yml"))):

        systems.append()
    return systems
