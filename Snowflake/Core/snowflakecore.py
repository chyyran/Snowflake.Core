#coding=utf-8
from Snowflake.Core.utils.generalutils import GeneralUtils as gutils

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import Snowflake.Core.server as serv
import handler.stdstreams as stdstrm

def main():
    gutils.server_log("Snowflake Core Started at " + gutils.get_datestring())
    #server = StreamServer(('', 6993), serv.handle_echo)
    #server.serve_forever()
    #handler = serv.SnowflakeServer()
    handler = stdstrm.run()
    #print "test"


if __name__ == '__main__':
    main()
