
import socket 

tcpclient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcpclient.connect(('127.0.0.1',1234))

cmd=str(input("enter command to execute on the server"))
tcpclient.send(cmd.encode())

response=tcpclient.recv(4096).decode()


print(response)

tcpclient.close()
