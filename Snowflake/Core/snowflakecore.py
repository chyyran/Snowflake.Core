#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import Snowflake.Core.server as serv
from Snowflake.Core.snowflakeutils import GeneralUtils as gutils


def main():
    gutils.server_log("Snowflake Core Started at " + gutils.get_datestring())
    #server = StreamServer(('', 6993), serv.handle_echo)
    #server.serve_forever()
    handler = serv.SnowflakeServer()
    print "test"


if __name__ == '__main__':
    main()
