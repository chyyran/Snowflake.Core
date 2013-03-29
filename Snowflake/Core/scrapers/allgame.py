#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import urllib
import re
from Snowflake.Core.snowflakeutils import ScraperUtils as sutils


__scrapername__ = "AllGame"
__scraperauthor__ = ["Angelscry", "ron975"]
__scrapersite__ = "www.allgame.com"
__scraperdesc__ = "Scrapes ROM information from AllGame"
__scraperfanarts__ = False


def get_games_by_name(search):
    """
    Gets a list of games returned by search.
    :param search: String to search.
    """
    params = urllib.urlencode({'sql': search, 'opt1': 81})
    results = []
    try:
        f = urllib.urlopen('http://www.allgame.com/search.php', params)
        for line in f.readlines():
            if '"game.php?id=' in line:
                game = {}
                game["id"] = ''.join(re.findall('<a[^>]*id=(.*?)">', line))
                game["title"] = (''.join(re.findall('<a[^>]*>(.*?)</a>', line)))
            if '"platform.php?id=' in line:
                game["system"] = ''.join(re.findall('<a[^>]*>(.*?)</a>', line))
                results.append(game)
        return results
    except:
        return results


def get_games_with_system(game_name, system):
    params = urllib.urlencode({'sql': game_name, 'opt1': 81})
    results = []
    try:
        f = urllib.urlopen('http://www.allgame.com/search.php', params)
        for line in f.readlines():
            if '"game.php?id=' in line:
                game = {}
                game["id"] = ''.join(re.findall('<a[^>]*id=(.*?)">', line))
                game["title"] = sutils.format_html_codes(''.join(re.findall('<a[^>]*>(.*?)</a>', line)))
            if '"platform.php?id=' in line:
                game["system"] = ''.join(re.findall('<a[^>]*>(.*?)</a>', line))
                if game["system"].lower() == system.lower():
                    results.append(game)
        return results
    except:
        return results


def get_game_datas(game_id):
    gamedata = {
        'title': "",
        'genre': "",
        'release': "",
        'studio': "",
        'plot': ""
    }

    try:
        f = urllib.urlopen('http://www.allgame.com/game.php?id=' + game_id)
        page = str(f.readlines())
        game_genre = ''.join(re.findall('<a href="genre.php[^>]*>(.*?)</a>', page))
        if game_genre:
            gamedata["genre"] = game_genre
        release_date = re.findall('<h3>Release Date</h3>[^>]*>(.*?)</p>', page)
        if release_date:
            gamedata["release"] = release_date[0][-4:]
        game_studio = re.findall('<h3>Developer</h3>[^>]*>(.*?)</p>', page)
        if game_studio:
            p = re.compile(r'<.*?>')
            gamestudio = p.sub('', game_studio[0])
        if gamestudio:
            gamedata["studio"] = gamestudio.rstrip()
        plot = re.findall('<h2[^>]*>(.*?)</p>(.*?)<p>(.*?)</p>', page)
        if plot:
            p = re.compile(r'<.*?>')
            gamedata["plot"] = sutils.format_html_codes(p.sub('', plot[0][2]))
        return gamedata
    except:
        return gamedata


def get_game_boxart(game_id):
    try:
        f = urllib.urlopen('http://www.allgame.com/game.php?id=' + game_id)
        page = str(f.readlines())
        imgurl = re.findall('(?sm)(?<=<div class="image">)(.*?)(?=</div>)', page)[0]
        if imgurl:
            imgurl = re.findall('(?<=<img src=")(.*?)(?=")', imgurl)[0]
            return imgurl
        else:
            return None
    except:
        return None
