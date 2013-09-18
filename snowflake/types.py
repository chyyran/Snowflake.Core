#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import shortuuid


class Console():
    def __init__(self, displayname, consoleid, cmdline, rompaths, filetypes, scrapers, **metadata):
        self.displayname = displayname
        self.consoleid = consoleid
        self.cmdline = cmdline
        self.rompaths = rompaths
        self.filetypes = filetypes
        self.scrapers = scrapers
        self.metadata = metadata

    def get_media(self, type):
        return


class Game():
    def __init__(self, uuid, gamename, systemid, rompath, **metadata):
        if uuid is "":
            self.uuid = shortuuid.uuid()
        else:
            self.uuid = uuid
        self.gamename = gamename
        self.systemid = systemid
        self.rompath = rompath
        self.metadata = metadata








