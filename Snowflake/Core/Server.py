from gevent import socket
from gevent.server import StreamServer
from Snowflake.Core.Utils import GeneralUtils as util


class SnowflakeServer():

    def serverDispatch(self,sock, address):
        fp = sock.makefile()
        while True:
            line = fp.readline()
            if line:
                util.serverLog(line)
                fp.write(line)
                fp.flush()
            else:
                break
        sock.shutdown(socket.SHUT_WR)
        sock.close()

    def startServer(self,port):
        util.serverLog("Server started")
        server = StreamServer(('', int(port)), self.serverDispatch)
        server.serve_forever()

