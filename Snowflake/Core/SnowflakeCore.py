__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

from gevent import socket
from gevent.server import StreamServer

from Snowflake.Core.Datastructures.Console import Console
from Snowflake.Core.Utils.GeneralUtils import GeneralUtils as gutils


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


def main():
    c = Console("Super Nintendo Entertainment System", "/assets/SNES.png", "SNES")
    c2 = Console("Nintendo Entertainment System", "/assets/NES.png", "NES")
    #g = Game("Mario Bros", "Platformer", 1990, "/assets/SNES/Mario.png","/roms/Mario.smc","Nintendo","SNES")
    #a = []
    #gutils.add_to_list(a, c, c2)
    #print json.dumps(a)

    gutils.server_log("Snowflake Core Started")
    server = StreamServer(('', 6993), handle_echo)
    server.serve_forever()


if __name__ == '__main__':
    main()
