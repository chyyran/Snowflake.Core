#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import shortuuid


class System():
    def __init__(self, fullname, short_name, run, mediapath ,rom_paths, extensions, scrapers):
        self.fullname = fullname
        self.short_name = short_name
        self.run = run
        self.rom_paths = rom_paths
        self.extensions = extensions
        self.scrapers = scrapers
        self.mediapath = mediapath

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








