
#!/usr/bin/python3
import socket 

clientfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


clientfd.connect(('127.0.0.1',12346))

clientfd.send("hello server ".encode())

msg=clientfd.recv(4096).decode()

print("server sent a message : ",msg)

clientfd.close()



