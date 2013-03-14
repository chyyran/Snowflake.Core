#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import urllib
import re
from Snowflake.Core.snowflakeutils import ScraperUtils as sutils

__scrapername__ = "MobyGames"
__scraperauthor__ = ["Angelscry", "ron975"]
__scrapersite__ = "mobygames.com"
__scraperdesc__ = "Scrapes ROM information from MobyGames"
__scraperfanarts__ = True


def get_games_by_name(search):
    results = []
    try:
        f = urllib.urlopen('http://www.mobygames.com/search/quick?q=' + search.replace(' ', '+') + '&sFilter=1&sG=on')
        for line in f.readlines():
            if 'searchNumber' in line:
                split_games = re.findall('Game: (.*?)</span></div>', line)
        for games in split_games:
            game_title = re.findall('<a href="(.*?)">(.*?)</a>', games)
            split_versions = re.findall('nowrap"><a href="(.*?)">(.*?)</a> ', games)
            if split_versions:
                for version in split_versions:
                    game = {}
                    game["title"] = sutils.format_html_codes(game_title[0][1])
                    game["id"] = 'http://www.mobygames.com' + version[0]
                    game["gamesys"] = version[1]
                    results.append(game)
            else:
                game = {}
                game["title"] = sutils.format_html_codes(game_title[0][1].replace('&#x26;', '&').replace('&#x27;', "'"))
                one_version = re.findall('nowrap">(.*?) \(', games)
                game["id"] = 'http://www.mobygames.com' + game_title[0][0]
                game["gamesys"] = one_version[0]
                results.append(game)
        return results
    except:
        return results


def get_games_with_system(search, gamesys):
    platform = sutils.system_conversion(gamesys, sutils.GameSysColumns.MOBY_GAMES, sutils.GameSysColumns.SYSTEM_NAME)
    results = []
    try:
        f = urllib.urlopen('http://www.mobygames.com/search/quick?q=' + search.replace(' ',
                                                                                       '+') + '&p=' + platform + '&sFilter=1&sG=on')
        for line in f.readlines():
            if 'searchNumber' in line:
                split_games = re.findall('Game: (.*?)</span></div>', line)
        for games in split_games:
            game_title = re.findall('<a href="(.*?)">(.*?)</a>', games)
            split_versions = re.findall('nowrap"><a href="(.*?)">(.*?)</a> ', games)
            if split_versions:
                for version in split_versions:
                    game = {}
                    game["title"] = sutils.format_html_codes(game_title[0][1])
                    game["id"] = 'http://www.mobygames.com' + version[0]
                    game["gamesys"] = gamesys
                    results.append(game)
            else:
                game = {}
                game["title"] = sutils.format_html_codes(game_title[0][1])
                game["id"] = game_title[0][0]
                game["gamesys"] = gamesys
                results.append(game)
        return results
    except:
        return results


def get_game_datas(game_id):
    gamedata = {}
    gamedata["genre"] = ""
    gamedata["release"] = ""
    gamedata["studio"] = ""
    gamedata["plot"] = ""
    try:
        f = urllib.urlopen('http://www.mobygames.com' + game_id)
        page = f.read().replace('\r\n', '').replace('\n', '')
        game_genre = re.findall('<a href="/genre/(.*?)">(.*?)</a>', page)
        if game_genre:
            gamedata["genre"] = sutils.format_html_codes(game_genre[0][1])
        game_release = re.findall('/release-info">(.*?)</a>', page)
        if game_release:
            gamedata["release"] = game_release[1][-4:]
        game_studio = re.findall('Developed by(.*?)<a href="(.*?)">(.*?)</a>', page)
        if game_studio:
            gamedata["studio"] = sutils.format_html_codes(game_studio[0][2])
        game_plot = re.findall('Description</h2>(.*?)<div class', page)
        if game_plot:
            p = re.compile(r'<.*?>')
            gamedata["plot"] = sutils.format_html_codes(p.sub('', game_plot[0]))
        return sutils.format_html_codes(gamedata)
    except:
        return gamedata


def get_game_boxart(game_id, region="All"):
    covers = []
    try:
        f = urllib.urlopen('http://www.mobygames.com' + game_id + '/cover-art')
        page = f.read().replace('\r\n', '').replace('\n', '')
        countries = re.findall(
            'Countr(.*?)</td><td>&nbsp;:&nbsp;</td><td><span style="white-space: nowrap">(.*?) <img alt="(.*?)href="(.*?)"><img alt="(.*?)" border="0" src="(.*?)"',
            page)
        found = 0
        for index, country in enumerate(countries):
            if region == 'US' or 'Default':
                if (country[1] == 'Canada') | (country[1] == 'United States'):
                    found = found + 1
                    covers.append([country[5].replace('/small/', '/large/'), country[5], 'Cover ' + str(found)])
            if region == 'JP':
                if (country[1] == 'Japan'):
                    found = found + 1
                    covers.append([country[5].replace('/small/', '/large/'), country[5], 'Cover ' + str(found)])
            if region == 'EU':
                if (country[1] == 'Finland') | (country[1] == 'France') | (country[1] == 'Germany') | (
                    country[1] == 'Italy') | (country[1] == 'The Netherlands') | (country[1] == 'Spain') | (
                    country[1] == 'Sweden') | (country[1] == 'United Kingdom'):
                    found = found + 1
                    covers.append([country[5].replace('/small/', '/large/'), country[5], 'Cover ' + str(found)])
            if region == 'All':
                found = found + 1
                covers.append([country[5].replace('/small/', '/large/'), country[5], 'Cover ' + str(found)])
                allcovers = []
                for cover in covers:
                    allcovers.append(cover[0])
                return allcovers
        return covers[0][0]
    except:
        return covers[0][0]