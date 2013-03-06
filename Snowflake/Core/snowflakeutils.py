__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
from time import strftime, timezone
import sqlite3
import difflib


class CommandUtils:
    """
    params
    """

    @classmethod
    def get_consoles(cls):
        """
        Gets a list of consoles.
        Corresponding JSONAPI command is
        {
        "Command": "GetGames"
        "Params": []
        }
        :return: List of consoles
        """
        return None

    @classmethod
    def get_games(cls, console):
        """


        :param console:
        :return:
        """
        return None


class GeneralUtils:
    @classmethod
    def server_log(cls, string):
        """
        Logs string to stdout
        :rtype : object
        :param string:
        """
        print "[Snowflake.Core] " + str(string)

    def parse_command(self, file_stream, command):
        if command == "TestCommand":
            self.write_to_stream(file_stream, "Received Test Command\0")
            return "Received Test Command\0"

        return "Invalid Command"

    def write_to_stream(self, file_stream, string):
        file_stream.write(string)
        file_stream.flush()

    @classmethod
    def add_to_list(cls, list, *data):
        for datum in data:
            list.append(datum.__dict__)

    @classmethod
    def get_datestring(cls):
        """


        :return:
        """
        return strftime("%m.%d.%Y %H:%M:%S (UTC ") + cls.get_formatted_timezone_offset(timezone) + ")"


    @classmethod
    def get_formatted_timezone_offset(cls, timezone):
        """
        Formats the timezone offset provided by time.timezone into standard UTC timezone strings
        :param timezone:
        :return: formatted timezone string
        """

        #Divide by 60 twice to get timezone in hours, then reverse the positivity.
        timezone = timezone / 60 / 60 - 2 * timezone / 60 / 60
        if timezone >= 0:
            formatted_offset = "+" + str(timezone) + ":00"
        else:
            formatted_offset = str(timezone) + ":00"

        return formatted_offset


class ScraperUtils:
    class GameSysColumns:
        GAME_FAQS = "GameFAQs"
        THE_GAMES_DB = "TheGamesDB"
        MOBY_GAMES = "MobyGames"
        SYSTEM_NAME = "SystemName"
        SHORT_NAME = "ShortName"

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
                print "Executed " + query
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

    @classmethod
    def get_best_match(cls, game_list, game_name):
        best_match = {}
        best_ratio = 0
        for game in game_list:
            if difflib.SequenceMatcher(None, game["title"], game_name).ratio() > best_ratio:
                best_ratio = difflib.SequenceMatcher(None, game["title"], game_name).ratio()
                best_match = game

        return best_match

    @classmethod
    def get_match_by_threshold(cls, game_dict, game_name, match_threshold):

        return
