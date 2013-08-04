#coding=utf-8
from snowflake import scrapers

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import urllib
import re
import os
import yaml

__scrapername__ = "GameFAQs"
__scraperauthor__ = ["Angelscry", "ron975"]
__scrapersite__ = "www.gamefaqs.com"
__scraperdesc__ = "Scrapes ROM information from GameFAQs"
__scraperfanarts__ = True
__scraperpath__ = os.path.dirname(os.path.realpath(__file__))
__scrapermap__ = yaml.load(open(os.path.join(__scraperpath__, "scrapermap.yml")))


def get_games_by_name(search):
    results = []
    try:
        f = urllib.urlopen('http://www.gamefaqs.com/search/index.html?platform=0&game=' + search.replace(' ', '+'))
        gets = {}
        gets = re.findall(r'\s+?<a href="(.*?)"\s+?>(.*?)</a></td>', f.read().replace('\r\n', ''))
        for get in gets:
            game = {}
            system = get[0].split('/')
            game["id"] = get[0].split('/')[2].split('-')[0]
            game["title"] = scrapers.format_html_codes(get[1])
            game["system"] = system[1].upper()
            results.append(game)
        return results
    except:
        return results


def get_games_with_system(search, system):
    scraper_sysid = __scrapermap__[system]
    results = []
    try:
        f = urllib.urlopen('http://www.gamefaqs.com/search/index.html?platform={0}&game={1}'
            .format(scraper_sysid, search.replace(' ', '+')))
        gets = re.findall(r'\s+?<a href="(.*?)"\s+?>(.*?)</a></td>', f.read().replace('\r\n', ''))
        for get in gets:
            game = {}
            game["id"] = get[0].split('/')[2].split('-')[0]
            game["title"] = scrapers.format_html_codes(get[1])
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
        f = urllib.urlopen("http://www.gamefaqs.com/" + str(game_id))
        page = f.read().replace('\r\n', '')
        game_genre = re.findall(r'</a> &raquo; <a href="(.*?)">(.*?)</a> &raquo; <a href="/', page)
        if game_genre:
            gamedata["genre"] = game_genre[0][1]
        game_release = re.findall(r'Release: <a href="(.*?)">(.*?) &raquo;</a>', page)
        if game_release:
            gamedata["release"] = game_release[0][1][-4:]
        game_studio = re.findall(r'<ul><li><a href="/features/company/(.*?)">(.*?)</a></li>', page)
        if game_studio:
            p = re.compile(r'<.*?>')
            gamedata["studio"] = p.sub('', game_studio[0][1])
        game_plot = re.findall(r'Description</h2></div><div class="body"><div class="details">(.*?)</div></div>', page)
        if game_plot:
            gamedata["plot"] = scrapers.format_html_codes(game_plot[0])
        return gamedata
    except:
        return gamedata


def get_game_boxart(game_id, region="Default"):
    covers = []
    try:
        game_page = urllib.urlopen('http://www.gamefaqs.com/' + str(game_id) + '/images?page=0')

        if game_page:
            for line in game_page.readlines():
                if 'pod contrib' in line:
                    results = re.findall(
                        '<div class="img boxshot"><a href="(.*?)"><img class="img100" src="(.*?)" alt="(.*?)" /></a>',
                        line)
        if (region == "Default" ):
            return results[0][1].replace('thumb', 'front')
        else:
            for result in results:
                if '(' + region + ')' in result[2]:
                    covers.append(result)
            return covers[0][1].replace('thumb', 'front')
    except:
        return covers