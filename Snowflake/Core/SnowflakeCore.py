__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

from gevent import socket
from gevent.server import StreamServer

from Snowflake.Core.Datastructures.Console import Console
from Snowflake.Core.Utils.GeneralUtils import GeneralUtils as gutils
from Snowflake.Core.Datastructures.Command import Command

import json
import datetime
import time
from time import gmtime
from time import strftime
from time import timezone


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
    cm = Command("GetGames", ["SNES", "Super Nintendo Entertainment System"])
    c = Console("Super Nintendo Entertainment System", "/assets/SNES.png", "SNES")
    c2 = Console("Nintendo Entertainment System", "/assets/NES.png", "NES")
    #g = Game("Mario Bros", "Platformer", 1990, "/assets/SNES/Mario.png","/roms/Mario.smc","Nintendo","SNES")
    #a = []
    #gutils.add_to_list(a, c, c2)
    #print json.dumps(a)
    print json.dumps(cm.__dict__)
    data = json.loads(json.dumps(cm.__dict__))
    cm = Command.command_from_dict(data)
    print cm.command

    for param in cm.params:
        print param
    gutils.server_log("Snowflake Core Started at "+gutils.get_datestring())
    server = StreamServer(('', 6993), handle_echo)
    server.serve_forever()


if __name__ == '__main__':
    main()
