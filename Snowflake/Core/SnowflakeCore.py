from gevent import socket
from gevent.server import StreamServer
from Snowflake.Core.Utils import GeneralUtils as gutils


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
    gutils.server_log("Snowflake Core Started")
    server = StreamServer(('', 6993), handle_echo)
    server.serve_forever()


if __name__ == '__main__':
    main()
