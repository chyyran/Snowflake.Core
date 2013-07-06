#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import shortuuid
import json

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
    def __init__(self, game_name, system_id, rom_path, media_path, **metadata):
        self.uuid = str(shortuuid.uuid())
        self.game_name = game_name
        self.system_id = system_id
        self.rom_path = rom_path
        self.media_path = media_path
        self.metadata = metadata
        self.json = json.dumps(metadata)

    def get_metadata(self, metadata_type):
        return self.metadata[metadata_type]






