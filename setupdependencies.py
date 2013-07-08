#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import subprocess

try:
    with open("pip-script.py"):
        subprocess.call("python pip-script.py install pyyaml")
        subprocess.call("python pip-script.py install jsonrpclib")
        subprocess.call("python pip-script.py install shortuuid")
        exit()
except IOError:
    print "Please run where pip is installed"
    print "Press Enter to continue"
    raw_input()
    exit()
