from django.shortcuts import render
from django.http import HttpResponse

import socket

DEFAULT_TIMEOUT=15
#HOST="127.0.0.0"
HOST="172.26.8.5"
PORT=25565

def index(reqauest):
    # set default context
    context = { "message" : "", "players_now" : "n/a", "players_max" : "n/a" }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # wait for connect up to 15sec
        s.settimeout(DEFAULT_TIMEOUT)
        if (s.connect_ex((HOST, PORT)) == 0):
            try:
                s.sendall(b"\xfe")

                #receive data and parse the server realm
                data = s.recv(2048)
                # remove leading b' and ' at the end
                data = str(data)[2:-1].replace("\\x00", "") \
                                        .replace("\\xff", "") \
                                        .split("\\xa7")

                context["message"] = f"Server realm: {data[0]}"
                context["players_now"] = str(data[1])
                context["players_max"] = str(data[2])

                #print(f"Server realm: {data[0]}, Players/max: {data[1]}/{data[2]}")
            except:
                context["message"] = f"Can't parse response from server : {data.__str__()}"
                #print("Can't parse response from server")
                #sys.exit(2)
        else:
            context["message"] = "Can't connect to the host/server!"
            #print("Can't connect to the host/server!")
            #sys.exit(1)

        return HttpResponse(context.__str__())

