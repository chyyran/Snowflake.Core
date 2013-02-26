__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""
from time import strftime, timezone


class GeneralUtils():
    @classmethod
    def server_log(cls, string):
        """
        Logs string to stdout
        :rtype : object
        :param string:
        """
        print "[Snowflake.Core] " + str(string)

    def parse_command(self, file_stream, command):
        if command == "TestCommand":
            self.write_to_stream(file_stream,"Received Test Command\0")
            return "Received Test Command\0"

        return "Invalid Command"

    def write_to_stream(self, file_stream, string):
        file_stream.write(string)
        file_stream.flush()

    @classmethod
    def add_to_list(cls, list, *data):
        for datum in data:
            list.append(datum.__dict__)

    @classmethod
    def get_datestring(cls):
        """


        :return:
        """
        return strftime("%m.%d.%Y %H:%M:%S (UTC ") + cls.get_formatted_timezone_offset(timezone) +" ) "


    @classmethod
    def get_formatted_timezone_offset(cls, timezone):
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
