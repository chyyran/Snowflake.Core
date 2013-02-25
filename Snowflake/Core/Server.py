__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

from gevent import socket
from gevent.server import StreamServer
from Snowflake.Core.Utils.GeneralUtils import GeneralUtils as util


class SnowflakeServer():
    def serverDispatch(self, sock, address):
        fp = sock.makefile()

        while True:
            line = fp.readline()
            if line:
                util.serverlog(line)
                util.parseCommand(fp, "Hello")
                #fp.write("Received Handshake")
                #fp.flush()
            else:
                break
        sock.shutdown(socket.SHUT_WR)
        sock.close()

    def startServer(self,port):
        util.serverlog("Server started")
        server = StreamServer(('', int(port)), self.serverDispatch)
        server.serve_forever()


