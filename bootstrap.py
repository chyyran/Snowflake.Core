#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "snowflake"))
import snowflake.core
print "Starting Snowflake"
snowflake.core.main()