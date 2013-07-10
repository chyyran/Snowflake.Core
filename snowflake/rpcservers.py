#coding=utf-8

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
from threading import Thread
from SimpleXMLRPCServer import SimpleXMLRPCServer
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from snowflake import rpcmethods

from inspect import getmembers, isfunction


class SnowflakeRPC:
    servers = []
    threads = []

    def __init__(self ,xmlport, jsonport):
        self.servers.append(SimpleXMLRPCServer(('localhost', xmlport)))
        self.servers.append(SimpleJSONRPCServer(('localhost', jsonport)))

        for server in self.servers:
            server.register_introspection_functions()
            #todo Make this dynamic, with config
            for function in getmembers(rpcmethods):
                if isfunction(function[1]):
                    if hasattr(function[1], "__rpcname__"):
                        server.register_function(function[1],function[1].__rpcname__)

    def start(self):
        self.threads.append(Thread(target=self.servers[0].serve_forever))
        self.threads.append(Thread(target=self.servers[1].serve_forever))
        for thread in self.threads:
            thread.start()

