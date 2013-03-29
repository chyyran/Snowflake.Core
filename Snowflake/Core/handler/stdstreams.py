#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import json
from Snowflake.Core.snowflakeutils import CommandUtils
from Snowflake.Core.command import executor

def run():
    while True:

        cmd = raw_input()
        command = CommandUtils.process_cmd(cmd)
        print json.dumps(executor.run_command(command))

