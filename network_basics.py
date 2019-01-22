

#!/usr/bin/python3
import socket 

serverfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverfd.bind(('127.0.0.1',12346))

serverfd.listen(5)

clientfd,addressinfo=serverfd.accept()

msg=clientfd.recv(4096).decode()

print("client sent a msg : ",msg )

clientfd.send("hello i am server".encode())

clientfd.close()
serverfd.close()


