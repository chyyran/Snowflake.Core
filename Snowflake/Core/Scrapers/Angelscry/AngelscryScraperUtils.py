__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import sqlite3


class AngelscryScraperUtils:

    @classmethod
    def json_to_sqlite(cls):
        import json
        """
        Converts the json to an sqlite database.
        Only present in code for demonstration. Do not invoke this method.
        JSON was produced from the original CSV by use of a header line deduced by hand and an online converter
        """
        jsonfile = open("assets/gamesys.json")
        data = json.load(jsonfile)
        con = None
        try:
            con = sqlite3.connect("assets/gamesys.db")
            cur = con.cursor()
            for datum in data:
                query = str("INSERT INTO gamesys VALUES('{0}',NULL,'{1}','{2}','{3}')").format(str(
                    datum["SystemName"]).replace('\'', '\'\''),
                                                                                               datum["GameFAQs"],
                                                                                               datum["MobyGames"],
                                                                                               datum["TheGamesDB"])
                cur.execute(query)
                print "Executed "+query
            con.commit()
            print "Commited SQL"
        except sqlite3.Error, e:
            print "Failed to insert JSON into Database" + e.args[0]

    @classmethod
    def system_conversion(cls, system_id, scraper_site, search_column):
        """
        Replaces _system_conversion in Angelscry's unmodified scrapers.
        Uses a SQLite3 database rather than the default CSV for speed and constancy
        :param system_id: Search string, for example "Nintendo Entertainment System". For reference, check gamesys.json
        :param scraper_site: Scraper column, recommended to use a GameSysColumn constant, eg GameSysColumns.GAME_FAQS
        :param search_column: Column to search for. Currently, only GameSysColumn.SYSTEM_NAME, works.
        :rtype : str
        """
        con = sqlite3.connect('assets/gamesys.db')
        cur = con.cursor()
        cur.execute("SELECT {0} FROM gamesys WHERE {1} = '{2}'".format(scraper_site, search_column, system_id))
        data = cur.fetchone()
        try:
            return data[0]
        except TypeError:
            return ''



class GameSysColumns:
    GAME_FAQS = "GameFAQs"
    THE_GAMES_DB = "TheGamesDB"
    MOBY_GAMES = "MobyGames"
    SYSTEM_NAME = "SystemName"
    SHORT_NAME = "ShortName"
