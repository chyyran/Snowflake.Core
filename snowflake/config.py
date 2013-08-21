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


def get_systems():

    """
    Gets systems from systems.yml
    :return: A dictionary of systems with the Snowflake system ID as key.
    """
    systems = {}
    for system in yaml.load(open(os.path.join(constants.directory_data, "systems.yml"))):
        systems[system["systemid"]] = System(**system)
    return systems
