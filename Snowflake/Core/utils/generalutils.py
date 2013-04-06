#coding=utf-8
import mimetypes
import os
from time import strftime, timezone
import urllib
import Snowflake

__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""


class GeneralUtils:

    @staticmethod
    def parse_command(file_stream, command):
        if command == "TestCommand":
            GeneralUtils.write_to_stream(file_stream, "Received Test Command\0")
            return "Received Test Command\0"
        return "Invalid Command"

    @staticmethod
    def get_core_directory():
        return os.path.dirname(Snowflake.Core.__file__)

    @staticmethod
    def download_file(url, directory, filename, extension=None):
        GeneralUtils.check_directory(directory)
        if extension is None:
            extension = GeneralUtils.get_extension_from_url(url)
        path = os.path.join(directory, filename) + str(extension)
        try:
            urllib.urlretrieve(url, path)
            return path
        except:
            return path

    @staticmethod
    def check_directory(path):
        try:
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise

    @staticmethod
    def get_extension_from_url(url):
        try:
            extension = mimetypes.guess_extension(mimetypes.guess_type(url)[0])
        except AttributeError:
            extension = ".html"
        return extension

    @staticmethod
    def server_log(string):
        """
        Logs string to stdout
        :rtype : object
        :param string:
        """
        print "[Snowflake.Core] " + str(string)


    @staticmethod
    def write_to_stream(self, file_stream, string):
        file_stream.write(string)
        file_stream.flush()

    @staticmethod
    def add_to_list(list, *data):
        for datum in data:
            list.append(datum.__dict__)

    @staticmethod
    def get_datestring():
        """
        :return:
        """
        return strftime("%m.%d.%Y %H:%M:%S (UTC ") + GeneralUtils.get_formatted_timezone_offset(timezone) + ")"


    @staticmethod
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