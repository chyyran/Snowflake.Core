#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import shortuuid
import json

class Console():
    def __init__(self, fullname, shortname, id, run, mediapath, rompaths, extensions, scrapers):
        self.fullname = fullname
        self.shortname = shortname
        self.id = id
        self.run = run
        self.mediapath = mediapath
        self.rompaths = rompaths
        self.extensions = extensions
        self.scrapers = scrapers


class Game():
    def __init__(self, title, console_id, rom_path, media_path, description, **metadata):
        self.uuid = str(shortuuid.uuid())
        self.title = title
        self.console_id = console_id
        self.rom_path = rom_path
        self.media_path = media_path
        self.description = description
        self.metadata = metadata


