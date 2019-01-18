import socket

# verifying mail username  on smtp server 

#creating client socket 
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#setting smtp server ip and port
sip=str(input("enter smtp server to send VRFY  req"))
spo=int(input("enter port that number of that smtp server,default =25"))

#connecting to smtp server
c.connect((sip,spo))

#recieving banner(info) of smtp
msg=c.recv(2048)
print("Banner grabbed : ",msg)

#enter username to check  if it exists on that smtp server
username=str(input("enter username u want to check"))

#sending username to smtp via VRFY command,u can also use EXPN command
#c.send("VRFY" + username).encode()
msg1="VRFY "+username
c.send(msg1.encode())
#recieving the response
res=c.recv(2048)


if 550 in res:
    print("username is not found")

elif 551 in res:
    print("user is not local")
elif 553 in res:
    print("user ambiguous")
elif 250 in res:
    print("user found")
elif 251 in res:
    print("mail to this address is forwarded")
elif 252 in res:
    print("server dont know about this username")


print(res)
c.close()
