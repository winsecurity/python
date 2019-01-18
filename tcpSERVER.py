import socket

#creating a socket object
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#defining server's(ours) ip address and port we want to listen
host="127.0.01"
port=1998

#binding socket 
ss.bind((host,port))

print("Listening for Connections....")
#listen up for one connection
ss.listen(1)

#accepting any incoming connection from client
cs,address=ss.accept()

#now connection has established
print("got connection from "+str(address))

while True:
    msg=cs.recv(1024).decode("utf-8")
    if not msg:
        break
    print("got msg - "+msg)
    msg=msg.upper()
    cs.send(msg.encode("utf-8"))
cs.close()
ss.close()
    



