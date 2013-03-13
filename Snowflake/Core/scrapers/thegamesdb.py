#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import urllib
import re
from Snowflake.Core.snowflakeutils import ScraperUtils as sutils


__scrapername__ = "TheGamesDB"
__scraperauthor__ = ["Angelscry", "ron975"]
__scrapersite__ = "thegamesdb.net"
__scraperdesc__ = "Scrapes ROM information from TheGamesDB.net API"
__scraperfanarts__ = True


def get_games_by_name(search):
    params = urllib.urlencode({"name": search})
    results = []
    try:
        f = urllib.urlopen("http://thegamesdb.net/api/GetGamesList.php", params)
        page = f.read().replace("\n", "")
        games = re.findall("<Game><id>(.*?)</id><GameTitle>(.*?)</GameTitle>(.*?)<Platform>(.*?)</Platform></Game>",
                           page)
        for item in games:
            game = {}
            game["id"] = "http://thegamesdb.net/api/GetGame.php?id=" + item[0]
            game["title"] = item[1]
            game["system"] = item[3]
            game["order"] = 1
            if game["title"].lower() == search.lower():
                game["order"] += 1
            if game["title"].lower().find(search.lower()) != -1:
                game["order"] += 1
            results.append(game)
        results.sort(key=lambda result: result["order"], reverse=True)
        return results
    except:
        return results


def get_games_with_system(search, system):
    platform = sutils.system_conversion(system, sutils.GameSysColumns.THE_GAMES_DB)
    params = urllib.urlencode({"name": search, "platform": platform})
    results = []
    try:
        f = urllib.urlopen("http://thegamesdb.net/api/GetGamesList.php", params)
        page = f.read().replace("\n", "")
        if platform == "Sega Genesis":
            params = urllib.urlencode({"name": search, "platform": "Sega Mega Drive"})
            f2 = urllib.urlopen("http://thegamesdb.net/api/GetGamesList.php", params)
            page = page + f2.read().replace("\n", "")
        games = re.findall("<Game><id>(.*?)</id><GameTitle>(.*?)</GameTitle>(.*?)<Platform>(.*?)</Platform></Game>",
                           page)
        for item in games:
            game = {}
            game["id"] = item[0]
            game["title"] = item[1]
            game["system"] = system
            game["order"] = 1
            if game["title"].lower() == search.lower():
                game["order"] += 1
            if game["title"].lower().find(search.lower()) != -1:
                game["order"] += 1
            if sutils.system_conversion(item[3], sutils.GameSysColumns.SYSTEM_NAME,
                                        sutils.GameSysColumns.THE_GAMES_DB).lower() == system.lower():
                results.append(game)
        results.sort(key=lambda result: result["order"], reverse=True)
        return results
    except:
        return results


def get_game_datas(game_id):
    gamedata = {
        'genre': "",
        'release': "",
        'studio': "",
        'plot': ""
    }

    try:
        f = urllib.urlopen("http://thegamesdb.net/api/GetGame.php?id=" + game_id)
        page = f.read().replace('\n', '')
        game_genre = ' / '.join(re.findall('<genre>(.*?)</genre>', page))
        if game_genre:
            gamedata["genre"] = sutils.remove_html_codes(game_genre)
        game_release = ''.join(re.findall('<ReleaseDate>(.*?)</ReleaseDate>', page))
        if game_release:
            gamedata["release"] = sutils.remove_html_codes(game_release[-4:])
        game_studio = ''.join(re.findall('<Developer>(.*?)</Developer>', page))
        if game_studio:
            gamedata["studio"] = sutils.remove_html_codes(game_studio)
        game_plot = ''.join(re.findall('<Overview>(.*?)</Overview>', page))
        if game_plot:
            gamedata["plot"] = sutils.remove_html_codes(game_plot)

        return gamedata
    except:
        return None


def get_game_boxart(game_id):
    try:
        f = urllib.urlopen("http://thegamesdb.net/api/GetGame.php?id=" + str(game_id))
        page = f.read().replace('\n', '')
        boxarts = re.findall(r'<boxart side="front" (.*?)">(.*?)</boxart>', page)[0][1]
        boxarts = "http://thegamesdb.net/banners/" + boxarts
        return boxarts
    except:
        return None
