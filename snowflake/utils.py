#coding=utf-8
import mimetypes
import os
from time import strftime, timezone
import urllib

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


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
    print "[Snowflake.Core {0}]".format(strftime("%H:%M:%S")), ' '.join(string)
