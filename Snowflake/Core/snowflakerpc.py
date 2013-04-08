#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
from threading import Thread
from SimpleXMLRPCServer import SimpleXMLRPCServer

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

import Snowflake

class SnowflakeRPC:
    servers = []
    threads = []

    def __init__(self ,xmlport, jsonport):
        self.servers.append(SimpleXMLRPCServer(('localhost', xmlport)))
        self.servers.append(SimpleJSONRPCServer(('localhost', jsonport)))
        for server in self.servers:
            server.register_function(Snowflake.Core.snowflakeapi.scrape_games,'ScrapeGames')
            server.register_function(Snowflake.Core.snowflakeapi.get_consoles,'GetConsoles')

    def start(self):
        self.threads.append(Thread(target=self.servers[0].serve_forever))
        self.threads.append(Thread(target=self.servers[1].serve_forever))
        for thread in self.threads:
            thread.start()

