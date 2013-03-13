#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

from gevent import socket
from gevent.server import StreamServer
from snowflakeutils import GeneralUtils as gutils


class SnowflakeServer():
    def __init__(self):
        self.server = StreamServer(('', 6993), SnowflakeServer.handle_echo)
        self.init_handler()

    @staticmethod
    def handle_echo(self, sock, address):
        fp = sock.makefile()
        while True:

            line = fp.readline().strip()
            if line:
                print "Received Command ", line

                gutils.parse_command(fp, line)
                gutils.write_to_stream(fp, "Command ReceivedXX")
                gutils.write_to_stream(fp, "Command ReceivedXY")

            else:
                break
        sock.shutdown(socket.SHUT_WR)
        sock.close()

    def init_handler(self):
        gutils.server_log("[Handler] Socket Handler Started")
        self.server.serve_forever()


