#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
import sys
try:
    sys.path.append(sys.argv[1])
except:
    pass

import Snowflake.Core.snowflakecore as snowflake_core


snowflake_core.main()

