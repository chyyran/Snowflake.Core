__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import urllib
import re


def get_games_list(search):
    params = urllib.urlencode({'sql': search, 'opt1': 81})
    results = []
    display = []
    try:
        f = urllib.urlopen('http://www.allgame.com/search.php', params)
        for line in f.readlines():
            if '"game.php?id=' in line:
                game = {}
                game["id"] = ''.join(re.findall('<a[^>]*id=(.*?)">', line))
                game["title"] = (''.join(re.findall('<a[^>]*>(.*?)</a>', line)))
            if '"platform.php?id=' in line:
                game["gamesys"] = ''.join(re.findall('<a[^>]*>(.*?)</a>', line))
                results.append(game)
                display.append(game["title"] + " / " + game["gamesys"])
        return results, display
    except:
        return results, display
