class GeneralUtils:

    @staticmethod
    def serverLog(string):
        """
        Logs string to stdout
        :rtype : object
        :param string:
        """
        print "[Snowflake.Core] " + str(string)