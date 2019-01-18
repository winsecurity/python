import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='192.168.0.103'
port = 8000
s.bind((' ',port))
s.listen(1000)
clients =[]
msg="Thanks for connecting to this server"


print("Listening for connections....")
while True:
    c,addr = s.accept()
    print(addr," connected")
    clients.append(addr)
    c.send(msg.encode())
    
    


s.close()

