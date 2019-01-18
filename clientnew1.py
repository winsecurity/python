import socket
import sys

#ip=sys.argv[1]
#port=sys.argv[2]
ip="127.0.0.1"
port=1300
mycs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mycs.connect((ip,port))

msg=mycs.recv(2048)
print("server message : ",msg)
newmsg=str(input("enter message to send"))
while newmsg!='Bye':
    
    mycs.send(newmsg.encode())
    smsg=mycs.recv(2048).decode()
    print("server replied : ",msg)
    newmsg=str(input("enter message to send"))
    
mycs.close()
