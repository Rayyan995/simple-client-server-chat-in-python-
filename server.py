from socket import *

s = socket(family=AF_INET, type=SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

host = "127.0.0.1"
port = 7000
server_addr = (host, port) #tuple to hold th server address

print("binding...")
s.bind(server_addr)

print("listening...")
s.listen(5) # 5 is number of clients that the server can listen to 

c, client_addr = s.accept()
print("connected to ", client_addr)

while True:
    c.send(input("Server: ").encode("UTF-8"))
    x = c.recv(500)
    print("Client says: ", x.decode('utf-8'))
close()
