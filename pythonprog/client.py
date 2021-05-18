import socket            

s = socket.socket()         

# Define the port on which you want to connect
port = 80              

s.connect(('localhost', 9996))
s.send(bytes("hand.jpeg","utf-8"))
f=open("back.jpeg","rb")
data=f.read(512)
while data:
    s.send(data)
    data=f.read(512)
f.close()
print(s.recv(10))
