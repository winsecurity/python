
#!/usr/bin/env python
import socket 
import subprocess
tcpserver=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpserver.bind(('127.0.0.1',1234))

tcpserver.listen(1)

clientsd,addressinfo=tcpserver.accept()

request=clientsd.recv(4096).decode()

print("Client requested command  : ",request)

cmd=subprocess.run([request],stdout=subprocess.PIPE)
output=cmd.stdout.decode('UTF-8')

clientsd.send(output.encode())

clientsd.close()
tcpserver.close()
