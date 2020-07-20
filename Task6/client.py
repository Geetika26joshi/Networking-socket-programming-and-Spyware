#Geetika Joshi
#2019h1030124h



import socket

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
with open('received_file.py', 'wb') as f:
    print 'file opened'
    while True:
        
        data = s.recv(BUFFER_SIZE)
        if not data:
            f.close()
            print 'file close()'
            break
       
        f.write(data)

print('Successfully get the file')
s.close()
print('connection closed')
