import socket

def TcpServer(host,port):

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    s.bind((host,port))
    s.listen(1)

    c,addr=s.accept()

    #print("got connection from"+str(c))

    msg="i am server at "+host

    cmsg=c.recv(2048).decode("utf-8")
    print(cmsg)
    c.send(msg.encode("utf-8"))
    c.close()
    s.close()

host=input("Enter ip addr in which want to start TCP Server")
port=int(input("Enter port of TCP Server"))
TcpServer(host,port)
