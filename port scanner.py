import socket

#ip=str(input("enter ip address"))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#define your ports here
ports=[21,22,23,25,80,443,8080]


def checkPorts(ip,ports):
    for each in range(0,len(ports)):
        try:
            x=ports[each]
            s.connect((ip,x))
        except Exception as e:
            print(x," was closed")
        else:
            print(x," was opened")


def checkAllPorts(ip):
    for port in range(0,65536):
        try:
            s.connect((ip,port))
        except Exception as e:
            print(port," was closed")
        else:
            print(port," was opened")


checkPorts("192.168.3.132",ports)
#checkAllPorts("192.168.3.132")
s.close()
