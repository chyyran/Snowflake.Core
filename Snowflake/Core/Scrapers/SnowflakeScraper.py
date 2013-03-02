__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import abc


class SnowflakeScraper:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_game_description(self, game_name, system):
        """Gets description for a game"""
        return

    @abc.abstractmethod
    def get_game_name(self, rom_name, system ):
        """Gets formatted game name from rom filename"""
        return

    @abc.abstractmethod
    def get_game_boxart(self, game_name, system):
        """Gets boxart URL for the game"""
        return

    @abc.abstractmethod
    def get_game_datas(self, game_name, system):
        """Gets data (release year, date, etc) for the game"""
        return