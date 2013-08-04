#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import os
from time import strftime, timezone

import snowflake


#Directories
directory_core = os.path.dirname(os.path.realpath(snowflake.__file__))
directory_data = os.path.join(directory_core, "data")


#time
def format_timezone_offset(timezone):
    """
    Formats the timezone offset provided by time.timezone into standard UTC timezone strings
    :param timezone:
    :return: formatted timezone string
    """

    #Divide by 60 twice to get timezone in hours, then reverse the positivity.
    timezone = timezone / 60 / 60 - 2 * timezone / 60 / 60
    if timezone >= 0:
        formatted_offset = "+" + str(timezone) + ":00"
    else:
        formatted_offset = str(timezone) + ":00"

    return formatted_offset

time_datestring = strftime("%m.%d.%Y %H:%M:%S (UTC ") + format_timezone_offset(timezone) + ")"
time_timestring = strftime("%H:%M:%S")
