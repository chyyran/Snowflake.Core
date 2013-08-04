#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import utils
import constants
from snowflake.rpc.rpcservers import RPCServers


#Start this with bootstrap.py
def main():
    utils.server_log("Snowflake started", constants.time_datestring)
    rpc = RPCServers(6994, 6993)
    rpc.start()

if __name__ == '__main__':
    print "Do not start Snowflake directly."
    print "Instead, call main() after adding Snowflake 's directory to sys.path"
    print "See bootstrap.py"