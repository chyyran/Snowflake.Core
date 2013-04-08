#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

from snowflakerpc import SnowflakeRPC
import Snowflake.Core.utils.generalutils as generalutils
import Snowflake.Core.snowflakeapi

def main():
    generalutils.server_log("Snowflake Core Started at " + generalutils.get_datestring())
    #server = StreamServer(('', 6993), serv.handle_echo)
    #server.serve_forever()
    #handler = serv.SnowflakeServer()
    rpc = SnowflakeRPC(8080, 8081)
    rpc.start()

if __name__ == '__main__':
    main()
