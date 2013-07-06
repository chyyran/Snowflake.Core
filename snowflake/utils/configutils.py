#coding=utf-8
import os
import yaml
from snowflake.datastructures import Console
import snowflake.utils.generalutils as generalutils

__author__ = 'ron975'
"""
This file is part of Snowflake.snowflake
"""


def get_config():
    return yaml.load(open(os.path.join(generalutils.get_core_directory(), "config.yml")))


def get_console(search):
    for system in yaml.load(open(os.path.join(generalutils.get_core_directory(), "systems.yml"))):
        if search in [system["fullname"], system["shortname", system["id"]]]:
            return Console(**system)
    return None


def get_console_by_id(id):
    for system in yaml.load(open(os.path.join(generalutils.get_core_directory(), "systems.yml"))):
        if id == system["id"]:
            return Console(**system)
    return None


def get_all_consoles():
    consoles = []
    for system in yaml.load(open(os.path.join(generalutils.get_core_directory(), "systems.yml"))):

        consoles.append(get_console_by_id(system["id"]))
    return consoles
