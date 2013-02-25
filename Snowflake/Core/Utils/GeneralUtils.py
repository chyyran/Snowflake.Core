__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

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