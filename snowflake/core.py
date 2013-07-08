#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.snowflake
"""

import snowflake.utils.generalutils as generalutils

from snowflake.snowflakerpc import SnowflakeRPC


def main():
    generalutils.server_log("Snowflake started", generalutils.get_datestring())
    rpc = SnowflakeRPC(6994, 6993)
    rpc.start()


if __name__ == '__main__':
    main()
