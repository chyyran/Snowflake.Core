#coding=utf-8
import os
import yaml
from Snowflake.Core.datastructures import Console
import Snowflake.Core.utils.generalutils as generalutils

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


def get_config():
    return yaml.load(open(os.path.join(generalutils.get_core_directory(), "config.yml")))

def get_console_from_config(consolename):
    for system in yaml.load(open(os.path.join(generalutils.get_core_directory(), "systems.yml"))):
        if consolename in [system["consolename"], system["shortname"]]:
            return Console(system["consolename"],
                           system["shortname"],
                           system["table"],
                           system["run"],
                           system["imagepath"],
                           system["rompaths"],
                           system["extensions"],
                           system["scrapers"])
    return None

def get_all_consoles():
    consoles = []
    for system in yaml.load(open(os.path.join(generalutils.get_core_directory(), "systems.yml"))):

        consoles.append(get_console_from_config(system["consolename"]))
    return consoles
