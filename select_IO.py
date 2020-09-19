from socket import socket
from select import select

sock = socket()
sock.bind(("0.0.0.0",9000))
sock.listen(5)
sock.setblocking(False)
rlist = [sock]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for i in rs:
        if i is sock:
            print("要开始了吆")
            connfd,addr = sock.accept()
            connfd.setblocking(False)
            print(addr)
            rlist.append(connfd)
        else:
            data = i.recv(1024).decode()
            print(data)
            if not data:
                rlist.remove(i)
                continue
            wlist.append(i)
    for r in ws:
        r.send(b"ok")
        wlist.remove(r)

