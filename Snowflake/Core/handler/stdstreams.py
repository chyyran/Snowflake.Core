#coding=utf-8
from Snowflake.Core.utils.commandutils import CommandUtils

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import json
from Snowflake.Core.command import executor

def run():
    while True:

        cmd = raw_input()
        command = CommandUtils.process_cmd(cmd)
        print json.dumps(executor.run_command(command))

