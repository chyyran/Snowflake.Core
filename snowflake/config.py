#coding=utf-8
import os
import yaml

from snowflake import utils, constants
from snowflake.types import Console

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


def get_config():
    return yaml.load(open(os.path.join(constants.directory_core, "data.yml")))


def get_consoles():

    """
    Gets consoles from consoles.yml
    :return: A dictionary of consoles with the Snowflake system ID as key.
    """
    consoles = {}
    for console in yaml.load(open(os.path.join(constants.directory_data, "consoles.yml"))):
        consoles[console["consoleid"]] = Console(**console)
    return consoles
