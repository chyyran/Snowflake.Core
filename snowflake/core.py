#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import snowflake.utils.generalutils as generalutils

from snowflake.rpcservers import SnowflakeRPC


#Start this with bootstrap.py
def main():
    generalutils.server_log("Snowflake started", generalutils.get_datestring())
    rpc = SnowflakeRPC(6994, 6993)
    rpc.start()
