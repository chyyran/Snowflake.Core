#coding=utf-8

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import urllib
import re
import os
import yaml
from snowflake import systemcolumns
from snowflake.utils import scraperutils

__scrapername__ = "MobyGames"
__scraperauthor__ = ["Angelscry", "ron975"]
__scrapersite__ = "mobygames.com"
__scraperdesc__ = "Scrapes ROM information from MobyGames"
__scraperfanarts__ = True
__scraperpath__ = os.path.dirname(os.path.realpath(__file__))
__scrapermap__ = yaml.load(open(os.path.join(__scraperpath__, "scrapermap.yml")))


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
                    game["title"] = scraperutils.format_html_codes(game_title[0][1])
                    game["id"] = 'http://www.mobygames.com' + version[0]
                    game["system"] = version[1]
                    results.append(game)
            else:
                game = {}
                game["title"] = scraperutils.format_html_codes(game_title[0][1].replace('&#x26;', '&').replace('&#x27;', "'"))
                one_version = re.findall('nowrap">(.*?) \(', games)
                game["id"] = 'http://www.mobygames.com' + game_title[0][0]
                game["system"] = one_version[0]
                results.append(game)
        return results
    except:
        return results


def get_games_with_system(search, system):
    scraper_sysid = __scrapermap__[system]
    results = []
    try:
        f = urllib.urlopen('http://www.mobygames.com/search/quick?q=' + search.replace(' ', '+')
                           + '&p=' + scraper_sysid + '&sFilter=1&sG=on')
        for line in f.readlines():
            if 'searchNumber' in line:
                split_games = re.findall('Game: (.*?)</span></div>', line)
        for games in split_games:
            game_title = re.findall('<a href="(.*?)">(.*?)</a>', games)
            split_versions = re.findall('nowrap"><a href="(.*?)">(.*?)</a> ', games)
            if split_versions:
                for version in split_versions:
                    game = {}
                    game["title"] = scraperutils.format_html_codes(game_title[0][1])
                    game["id"] = 'http://www.mobygames.com' + version[0]
                    game["system"] = system
                    results.append(game)
            else:
                game = {}
                game["title"] = scraperutils.format_html_codes(game_title[0][1])
                game["id"] = game_title[0][0]
                game["system"] = system
                results.append(game)
        return results
    except:
        return results


def get_game_datas(game_id, title):
    gamedata = {
        'title': "",
        'genre': "",
        'release': "",
        'studio': "",
        'plot': ""
    }
    try:
        gamedata["title"] = title
        f = urllib.urlopen('http://www.mobygames.com' + game_id)
        page = f.read().replace('\r\n', '').replace('\n', '')
        game_genre = re.findall('<a href="/genre/(.*?)">(.*?)</a>', page)
        if game_genre:
            gamedata["genre"] = scraperutils.format_html_codes(game_genre[0][1])
        game_release = re.findall('/release-info">(.*?)</a>', page)
        if game_release:
            gamedata["release"] = game_release[1][-4:]
        game_studio = re.findall('Developed by(.*?)<a href="(.*?)">(.*?)</a>', page)
        if game_studio:
            gamedata["studio"] = scraperutils.format_html_codes(game_studio[0][2])
        game_plot = re.findall('Description</h2>(.*?)<div class', page)
        if game_plot:
            p = re.compile(r'<.*?>')
            gamedata["plot"] = scraperutils.format_html_codes(p.sub('', game_plot[0]))
        return scraperutils.format_html_codes(gamedata)
    except:
        return gamedata


def get_game_boxart(game_id, region="EU"):
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
                    found += 1
                    covers.append([country[5].replace('/small/', '/large/'), country[5], 'Cover ' + str(found)])
            if region == 'JP':
                if country[1] == 'Japan':
                    found += 1
                    covers.append([country[5].replace('/small/', '/large/'), country[5], 'Cover ' + str(found)])
            if region == 'EU':
                if country[1] in ['Finland', 'France', 'Germany', 'Italy', 'The Netherlands', 'Spain', 'Sweden',
                                  'United Kingdom']:
                    found += 1
                    covers.append([country[5].replace('/small/', '/large/'), country[5], 'Cover ' + str(found)])
            if region == 'All':
                found += 1
                covers.append([country[5].replace('/small/', '/large/'), country[5], 'Cover ' + str(found)])
                allcovers = []
                for cover in covers:
                    allcovers.append(cover[0])
                return allcovers
        return covers[0][0]
    except:
        return covers[0][0]