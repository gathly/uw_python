#!/usr/bin/python

import socket
import sys
import select
import datetime

def prompt():
    sys.stdout.write(':: ')
    sys.stdout.flush()

host = 'localhost'
port = 50009

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((host,port))
print 'connection accepted by (%s,%s)' % (host,port)
prompt()

input = [server, sys.stdin]
running = True
while running:
    inputready, outputready, exceptready = select.select(input, [],[],60)
    if not inputready:
        print 'chat client running at %s' % datetime.datetime.now()
        prompt()

    for s in inputready:
        if s == sys.stdin:
            msg = sys.stdin.readline().strip('\n')
            if msg:
                server.send(msg)
            else:
                server.close()
                running = False
        elif s:
                data = server.recv(1024)
                print data
                prompt() 
