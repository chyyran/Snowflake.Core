#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import json

from Snowflake.Core.command import cmdstr_parser, executor

def run():
    while True:
        cmd = raw_input()
        command = cmdstr_parser.parse(cmd)
        print json.dumps(executor.run_command(command))

