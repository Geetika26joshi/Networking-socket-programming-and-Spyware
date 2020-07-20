#Geetika Joshi
#2019h1030124h

import socket

(HOST,PORT)=('localhost',1029)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((HOST,PORT))
with open('xyz.py', 'rb') as f1:
  for l1 in f1: s.sendall(l1)
  f1.close()
  a = "done"
  s.send(a.encode('ascii'))
  
print("Done sending")

s.close()





'''
with open('vdo.mp4', 'rb') as f:
  for l in f: s.sendall(l)
  f.close()
  
print("Done sending")
'''


   # conn.send("Thank you for connecting")

