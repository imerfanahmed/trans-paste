import socket
c=socket.socket()

c.connect(('192.168.1.89',9989))


while(True):
    text=input("Type your Massage here= ")
    c.send(bytes(text,'utf-8'))
    print(c.recv(1024).decode())