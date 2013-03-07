__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

__scrapername__ = "SnowflakeScraper"
__scraperauthor__ = ["ron975"]
__scrapersite__ = "N/A"
__scraperdesc__ = "The interface in which all scrapers should be based upon."


def get_games_list(search):
    """Gets a list of games from search parameter"""
    return

def get_game_description(game_name, system):
    """Gets description for a game"""
    return


def get_game_name(id, system ):
    """Gets formatted game name from rom filename"""
    return


def get_game_boxart(game_id, system):
    """Gets boxart URL for the game"""
    return


def get_game_datas(game_id, system):
    """Gets data (release year, date, etc) for the game"""
    return


def get_first_game_object(game_name, system):
    """Gets the search object for each game"""
    return


def get_all_game_objects(game_name, system):
    """Returns a list of all game objects to loop"""
    return