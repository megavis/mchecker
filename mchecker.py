#!/usr/bin/env python3

# maintainer "ivanvernichenko@gmail.com"

import socket
import sys

import argparse

#HOST = "18.193.165.130"
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 25565
DEFAULT_TIMEOUT = 15

parser=argparse.ArgumentParser(description="Test Minecraft server for its health and return exit code then")
parser.add_argument("host", action="store", type=str, 
                            help="server hostname or IP")
parser.add_argument("-p", action="store", dest="port", type=int, 
                          default=DEFAULT_PORT, 
                          help="server port (default: 25565)", required=False)

args=parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # wait for connect up to 15sec
    s.settimeout(DEFAULT_TIMEOUT)
    if (s.connect_ex((args.host, args.port)) == 0):
        try:
            s.sendall(b"\xfe")

            #receive data and cleanup the server realm
            data = str(s.recv(2048)).replace("\\x00", "") \
                                    .replace("b\'\\xff/","") \
                                    .replace("'","") \
                                    .split("\\xa7")

            print(f"Server realm: {data[0]}, Players/max: {data[1]}/{data[2]}")
        except:
            print(f"Can't parse response from server")
            sys.exit(2)
    else:
        print("Can't connect to the host/server!")
        sys.exit(1)

    

