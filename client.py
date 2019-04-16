from socket import *

s = socket(family=AF_INET, type=SOCK_STREAM)

host = "127.0.0.1"
port = 7000

server_addr = (host, port)

s.connect(server_addr)
print('connected')

while True:
    x = s.recv(500)
    print('Server says: ', x.decode('utf-8'))
    s.send(input('Client: ').encode('utf-8'))

s.close()
