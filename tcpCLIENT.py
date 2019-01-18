import socket
import sys

#creating client socket
cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#defining host port of server to connect
host="192.168.3.137"
port=1234

#connecting to the server
cs.connect((host,port))

#now connection established

msg="hello server"

#sending our msg to sever

cs.send(msg.encode("utf-8"))
data=cs.recv(1024).decode("utf-8")
print("got msg from server : "+data)

cs.close()



