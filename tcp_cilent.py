from socket import socket

sock = socket()
sock.connect(("192.168.48.209",9000))

while True:
    data = input("请开始：")
    sock.send(data.encode())
    info = sock.recv(1024).decode()
    print(info)