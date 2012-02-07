on refused
UW-PYTHON$:
#!/usr/bin/python
import select
import socket
import datetime
import sys

host = ''
port = 50009
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host,port))
print 'chat server listening on ', port
server.listen(5)
running = True
input = [server,sys.stdin]
while running:
    inputready,outputready,exceptready = select.select(input,[],[],60)

    if not inputready:
        print 'server running at %s' % datetime.datetime.now()

    for s in inputready:
        if s == server:
            client, address = server.accept()
            input.append(client)
            print 'accepted connection from ', address

        elif s == sys.stdin:
            junk = sys.stdin.readline()
            running = False
            print 'Input %s from stdin, exiting.' % junk.strip('\n')

        elif s:
            id = s.getpeername()
            data = s.recv(1000)
            print '%s: %s' % (id, data)
            if data:
                for c in input:
                    if c != s and c != sys.stdin:
                        c.send('gathly %s: %s' % (id, data))
                    
            else:
                s.close()
            print 'closed connection'
            input.remove(s)
