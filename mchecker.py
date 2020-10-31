#!/usr/bin/env python3

# maintainer "ivanvernichenko@gmail.com"

import socket
import sys

HOST = "18.193.165.130"
PORT = 25565
CONN_TIMEOUT = 15

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # wait for connect up to 15sec
    s.settimeout(CONN_TIMEOUT)
    if (s.connect_ex((HOST, PORT)) == 0):
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

    

