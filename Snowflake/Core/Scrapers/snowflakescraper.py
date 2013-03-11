#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

__scrapername__ = "SnowflakeScraper"
__scraperauthor__ = ["ron975"]
__scrapersite__ = "N/A"
__scraperdesc__ = "The interface in which all scrapers should be based upon."


def get_games_by_name(search):
    """Gets a list of games from search parameter"""
    return


def get_game_boxart(game_id):
    """Gets boxart URL for the game"""
    return


def get_game_datas(game_id):
    """Gets data (release year, date, etc) for the game"""
    return


def get_games_with_system(game_name, system):
    """Returns a list of all game objects to loop"""
    return
