
import socket 

for i in range(1,100):

    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip = '192.168.0.100'
        port = i

        s.connect((ip,port))

        print(str(port)+" is opened")
        s.close()

    except:
        
        s.close()

