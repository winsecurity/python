import socket

#ip=input("enter ip address")
#port=int(input("enter open port of that server"))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.3.137',81))
msg=s.recv(2048)
print(msg)
