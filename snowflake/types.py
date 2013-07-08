#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.snowflake
"""

import shortuuid


class Console():
    def __init__(self, fullname, short_name,run, rom_paths, extensions, scrapers):
        self.fullname = fullname
        self.short_name = short_name
        self.run = run
        self.rom_paths = rom_paths
        self.extensions = extensions
        self.scrapers = scrapers

    def get_media(self, type):
        return


class Game():
    def __init__(self, uuid, gamename, systemid, rompath, mediapath, **metadata):
        if uuid is "":
            self.uuid = shortuuid.uuid()
        else:
            self.uuid = uuid
        self.gamename = gamename
        self.systemid = systemid
        self.rompath = rompath
        self.mediapath = mediapath
        self.metadata = metadata







