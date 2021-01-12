import socket
import pyperclip as p

s=socket.socket()
print("Socket Created Successfully")

s.bind(('192.168.1.89',9989))

print("Waiting for the clients")
s.listen(2)
while True:
    c,addr=s.accept()
    print("Connected with",addr)
    print(c.recv(1024).decode())
    p.copy(c.recv(1024).decode())