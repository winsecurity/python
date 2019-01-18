#importing socket module , this is core module for creating connections

import socket 
import sys
#getting server ip and port to connect 
host=str(input("Enter Server Ip Address"))
port=int(input("Enter corresponding port number"))

bind=(host,port)



#creating socket object

tc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tc.connect(bind)

tc.recv(msg)


