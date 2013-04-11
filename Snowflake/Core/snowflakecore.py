#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

from snowflakerpc import SnowflakeRPC
import Snowflake.Core.utils.generalutils as generalutils


def main():
    generalutils.server_log("Snowflake Core Started at " + generalutils.get_datestring())
    rpc = SnowflakeRPC(6994, 6993)
    rpc.start()


if __name__ == '__main__':
    main()
