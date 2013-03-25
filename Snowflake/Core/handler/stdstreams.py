#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

from Snowflake.Core.command.command import Command
def run():
    while True:
        cmd = raw_input()
        print process_cmd(cmd)

def process_cmd(cmd):
    command = cmd.split(':')

    return cmd