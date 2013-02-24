from gevent import socket
from gevent.server import StreamServer
from Snowflake.Core.Utils import GeneralUtils as gutils
from Snowflake.Core.Datastructures.Console import Console
from Snowflake.Core.Datastructures.Game import Game
import json
import array

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
    #c = Console("Super Nintendo Entertainment System", "/assets/SNES.png", "SNES")
    #c2 = Console("Nintendo Entertainment System", "/assets/NES.png", "NES")
    #g = Game("Mario Bros", "Platformer", 1990, "/assets/SNES/Mario.png","/roms/Mario.smc","Nintendo","SNES")
    #a = [c.__dict__,c2.__dict__]
    #print json.dumps(a)
    #print json.dumps(c.__dict__)
    #print json.dumps(g.__dict__)
    gutils.server_log("Snowflake Core Started")
    server = StreamServer(('', 6993), handle_echo)
    server.serve_forever()


if __name__ == '__main__':
    main()
