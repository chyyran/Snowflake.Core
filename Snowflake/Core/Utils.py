class GeneralUtils():

    @classmethod
    def server_log(cls, string):
        """
        Logs string to stdout
        :rtype : object
        :param string:
        """
        print "[Snowflake.Core] " + str(string)


    def parse_command(self, filestream, command):
        if command == "TestCommand":
            self.write_to_stream(filestream,"Received Test Command\0")
            return "Received Test Command\0"

        return "Invalid Command"

    def write_to_stream(self, filestream, string):
        filestream.write(string)
        filestream.flush()
