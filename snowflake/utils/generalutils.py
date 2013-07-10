#coding=utf-8
import mimetypes
import os
from time import strftime, timezone
import urllib
import snowflake

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


def get_core_directory():
    return os.path.dirname(snowflake.__file__)


def download_file(url, directory, filename, extension=None):
    check_directory(directory)
    if extension is None:
        extension = get_extension_from_url(url)
    path = os.path.join(directory, filename) + str(extension)
    try:
        urllib.urlretrieve(url, path)
        return path
    except:
        return path


def check_directory(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise


def get_extension_from_url(url):
    try:
        extension = mimetypes.guess_extension(mimetypes.guess_type(url)[0])
    except AttributeError:
        extension = ".html"
    return extension


def server_log(*string):
    """
    Logs string to stdout
    :rtype : object
    :param string:
    """
    print "[Snowflake.Core {0}]".format(get_timestring()), ' '.join(string)


def get_datestring():
    """
    :return:
    """
    return strftime("%m.%d.%Y %H:%M:%S (UTC ") + get_formatted_timezone_offset(timezone) + ")"


def get_timestring():
    return strftime("%H:%M:%S")


def get_formatted_timezone_offset(timezone):
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