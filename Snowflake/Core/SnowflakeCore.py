from Snowflake.Core.Utils import GeneralUtils as util
from Snowflake.Core.Server import SnowflakeServer as snowserver


def main():

    """
    serverLog("Snowflake Server Started")
    startServer(6993)
    """
    util.serverLog("hello")
    s = snowserver()
    s.startServer(6993)


if __name__ == "__main__":
    main()