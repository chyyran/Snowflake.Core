__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

class Game():
    def __init__(self, game_name, description, release_year, cover_path, rom_path, publisher, console_name):
        self.game_name = game_name
        self.description = description
        self.release_year = release_year
        self.cover_path = cover_path
        self.rom_path = rom_path
        self.publisher = publisher
        self.console_name = console_name