from socket import socket
from select import *

sock = socket()
sock.bind(("0.0.0.0", 9000))
sock.listen(5)
sock.setblocking(False)

p = poll()
map = {sock.fileno(): sock}
p.register(sock, POLLIN)
while True:
    events = p.poll()
    for fd, enevt in events:
        if fd == sock.fileno():
            print("要开始了吆")
            connfd, addr = map[fd].accept()
            connfd.setblocking(False)
            p.register(connfd,POLLIN)
            print(addr)
            map[connfd.fileno()] = connfd
        elif enevt == POLLIN:
            data = map[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                map[fd].close()
                del map[fd]
                continue
            print(data)
            p.register(fd,POLLOUT)
        elif enevt == POLLOUT:
            map[fd].send(b"ok")
            p.register(fd,POLLIN)
            p.unregister(fd)
