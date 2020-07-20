#Geetika Joshi
#2019h1030124h


import socket
import subprocess 
import os
from subprocess import call,STDOUT
(HOST,PORT) = ('localhost',1029)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)); 
s.listen(1); 
print ("Server listening....")
conn, addr = s.accept()
a="done"
b=a.encode("ascii")

s.listen(5)                     # Now wait for client connection.
#s.connect((host, port))

with open('Recieved.py','wb') as f:
  while True:
    #print("receiving data1...")
    l = conn.recv(50000)
    if l == b: 
        print("Recieved file 1")
        f.close()
        break
    f.write(l)


print("successfully get the file")
print('connection closed')

os.popen( "python Recieved.py")
