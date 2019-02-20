#upto now this program only works with GET requests , you can modify for browser requests

import socket
import sqlite3
import time
import re

def pushtodb(data,ip,domain):
    #add your database here
    connector=sqlite3.connect("logs.db")
    c=connector.cursor()
    timestamp=time.asctime(time.localtime())
    c.execute("""insert into logsinfo values (?,?,?,?)""",(timestamp,ip,data,domain))
    connector.commit()
    connector.close()


client_to_proxy=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_to_proxy.bind(("127.0.0.1",1234))
client_to_proxy.listen(1)

client,address=client_to_proxy.accept()

#print(client.getpeername())

request=client.recv(4096).decode()


#extracting url from GET request
print(request)
domain=re.compile(r'http[s]://\w\w\w\.[\w]+\.[\w]+')
browser_domain=re.compile(r'[\w]+\.\w\w\w')
print(browser_domain)
match=domain.finditer(request)
match2=browser_domain.finditer(request)
domain_name=""
for every in match:
    domain_name=every.group(0)
    print(domain_name)

#write your own desired function

pushtodb(request,client.getpeername()[0],domain_name)


#stripping protocol from url as sockets gets error when we use protocol
domain1=domain_name.replace('https://','')

print(domain1)

#creating socket which connects to server client wants to and sends response to client
proxy_to_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
proxy_to_server.connect((domain1,80))

index="""GET /index.html HTTP/1.1\n
        Hostname:"""+domain_name+"""\r\n\r\n"""
proxy_to_server.send(index.encode())
response=proxy_to_server.recv(4096).decode()
client.send(response.encode())


client.close()
client_to_proxy.close()
