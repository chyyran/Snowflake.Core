#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

from gevent import socket
from snowflakeutils import GeneralUtils as gutils


def handle_echo(sock, address):
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


