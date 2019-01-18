import socket
import sys


#port=sys.argv[1]
port=1300
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(("127.0.0.1",port))

ss.listen(1)
cs,address=ss.accept()
print("got connection  from : ",address)
cs.send("hi you are connected to my server")


while True:
    msg=cs.recv(2048).decode()
    print("message recieved ",msg)
    if msg=="Bye":
        print("replied message is ",msg," closing")
        cs.send(msg.encode())
        break
    else:
        newmsg=msg.upper()
        cs.send(newmsg.encode())
        print("replied message is ",newmsg)
        #msg=cs.recv(2048)
cs.close()
ss.close()

        
