#coding=utf-8
import difflib
import imp
import json
import os
import sqlite3
from Snowflake.Core import systemcolumns
from Snowflake.Core.scrapers import snowflakescraper as scraperbase, snowflakescraper
from Snowflake.Core.utils.generalutils import GeneralUtils

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


class ScraperUtils:
    @staticmethod
    def get_scrapers_directory():
        return os.path.dirname(os.path.realpath(scraperbase.__file__))

    @staticmethod
    def get_scraper(scrapername):
        scraper = imp.load_source('snowflake.{0}'.format(scrapername),
                                  os.path.join(ScraperUtils.get_scrapers_directory(), scrapername.lower() + ".py"))

        if scraper.__scrapername__.lower() != scrapername.lower():
            return scraperbase
        else:
            return scraper

    @staticmethod
    def __json_to_sqlite():
        """
        Converts the json to an sqlite database.
        Only present in code for demonstration. Do not invoke this method.
        JSON was produced from the original CSV by use of a header line deduced manually and an online converter
        """
        jsonfile = open(os.path.join(GeneralUtils.get_core_directory(), "assets", "systems.json"))
        data = json.load(jsonfile)
        con = None
        try:
            con = sqlite3.connect(os.path.join(GeneralUtils.get_core_directory(),"assets","systems.db"))
            cur = con.cursor()
            for datum in data:
                query = str("INSERT INTO systems VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')").format(str(
                    datum["SystemName"]).replace('\'', '\'\''),
                    datum["ShortName"],
                    datum["GameFAQs"],
                    datum["GameFAQs_URL"],
                    datum["MobyGames"],
                    datum["TheGamesDB"],
                    datum["GiantBomb"])
                cur.execute(query)
                print "Executed " + query
            con.commit()
            print "Commited SQL"
        except sqlite3.Error, e:
            print "Failed to insert JSON into Database: " + e.args[0]

    @staticmethod
    def system_conversion(system_id, scraper_site, search_column=systemcolumns.SYSTEM_NAME):
        """
        Replaces _system_conversion in Angelscry's unmodified scrapers.
        Uses a SQLite3 database rather than the default CSV for speed and constancy
        :param system_id: Search string, for example "Nintendo Entertainment System". For reference, check systems.json
        :param scraper_site: Scraper column, recommended to use a GameSysColumn constant, eg SystemColumns.GAME_FAQS
        :param search_column: Column to search for. Currently, only GameSysColumn.SYSTEM_NAME, works.
        :rtype : str
        """
        dbpath = os.path.join(GeneralUtils.get_core_directory(), "assets", "systems.db")
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute("SELECT {0} FROM systems WHERE {1} = '{2}'".format(scraper_site, search_column, system_id))
        data = cur.fetchone()
        try:
            return data[0]
        except TypeError:
            return ''

    @staticmethod
    def get_best_from_results(game_searches, game_name):
        best_match = {}
        best_ratio = 0
        for scraper, game_search in game_searches.iteritems():
            try:
                if difflib.SequenceMatcher(None, game_search["title"], game_name).ratio() > best_ratio:
                    best_ratio = difflib.SequenceMatcher(None, game_search["title"], game_name).ratio()
                    best_match = {"scraper": scraper, "search": game_search}
            except KeyError:
                pass

        return best_match

    @staticmethod
    def get_best_search_result(game_list, game_name):
        best_match = {}
        best_ratio = 0
        for game in game_list:
            if difflib.SequenceMatcher(None, game["title"], game_name).ratio() > best_ratio:
                best_ratio = difflib.SequenceMatcher(None, game["title"], game_name).ratio()
                best_match = game

        return best_match

    @staticmethod
    def get_match_by_threshold(game_dict, game_name, match_threshold):

        return


    @staticmethod
    def format_html_codes(s):
        """
        :author: Angelscry
        Replaces HTML character codes into their proper characters
        :return:
        """
        s = s.replace('<br />', ' ')
        s = s.replace("&lt;", "<")
        s = s.replace("&gt;", ">")
        s = s.replace("&amp;", "&")
        s = s.replace("&#039;", "'")
        s = s.replace('<br />', ' ')
        s = s.replace('&quot;', '"')
        s = s.replace('&nbsp;', ' ')
        s = s.replace('&#x26;', '&')
        s = s.replace('&#x27;', "'")
        s = s.replace('&#xB0;', "°")
        s = s.replace('\xe2\x80\x99', "'")
        return s