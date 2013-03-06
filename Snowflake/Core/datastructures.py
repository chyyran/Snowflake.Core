__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


class Command():
    def __init__(self, command, params=[]):
        self.command = command
        self.params = params

    @classmethod
    def command_from_dict(cls, dict):
        command = Command(dict["command"], dict["params"])
        return command


class Console():
    def __init__(self, console_name, image_path, short_name):
        self.console_name = console_name
        self.image_path = image_path
        self.short_name = short_name

    def __repr__(self):
        return self.console_name


class Game():
    def __init__(self, game_name, description, release_year, cover_path, rom_path, publisher, console_name):
        self.game_name = game_name
        self.description = description
        self.release_year = release_year
        self.cover_path = cover_path
        self.rom_path = rom_path
        self.publisher = publisher
        self.console_name = console_name