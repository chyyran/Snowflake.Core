#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


import Snowflake.Core.utils.scraperutils as scraperutils


def scrape_game(game_name, system, scrapers):

    searches = {}
    for scraper in scrapers:
        scraper = scraperutils.get_scraper(scraper)
        game_list = scraper.get_games_with_system(game_name, system)
        game_search = scraperutils.get_best_search_result(game_list, game_name)
        searches[scraper] = game_search
        #print searches
    best_search = scraperutils.get_best_from_results(searches, game_name)
    return best_search["scraper"].get_game_datas(best_search["search"]["id"], best_search["search"]["title"])
