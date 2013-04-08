#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import Snowflake.Core.utils.generalutils as generalutils
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import Snowflake.Core.snowflakeapi
def main():
    generalutils.server_log("Snowflake Core Started at " + generalutils.get_datestring())
    #server = StreamServer(('', 6993), serv.handle_echo)
    #server.serve_forever()
    #handler = serv.SnowflakeServer()
    server = SimpleJSONRPCServer(('localhost', 8080))
    server.register_function(Snowflake.Core.snowflakeapi.scrape_games,'ScrapeGames')
    server.register_function(Snowflake.Core.snowflakeapi.get_consoles,'GetConsoles')
    server.serve_forever()
    print "test"


if __name__ == '__main__':
    main()
