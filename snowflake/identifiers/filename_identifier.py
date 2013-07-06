#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.snowflake
"""
import re
import os


def identify_rom(rom_name):
    """
    Uses regex to strip anything inside parentheses, brackets, and extension.
    Removes standard GoodTools naming convention tags.
    Thanks to Ionut Hulub at StackOverflow for helping me with this regex.
    I suck at regex. Its like dark magic to me.
    """

    #Remove the extension before passing in regex
    rom_name = os.path.splitext(rom_name)[0]
    #Remove anything in brackets, parentheses
    return re.search(r'(\([^]]*\))*(\[[^]]*\])*([\w\.\-\s]+)', rom_name).group(3)