import socket
import pyperclip as p

s=socket.socket()
print("Socket Created Successfully")

s.bind(('192.168.1.89',9989))

print("Waiting for the clients")
s.listen(2)
c,addr=s.accept()
print("Connected with",addr)

while True:
    data=c.recv(10000).decode()
    print(data)
    p.copy(data)

