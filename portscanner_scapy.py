import scapy
from scapy.all import *

address=input("enter ip address to check ports")
port=int(input("enter port number "))

ip=IP()
ip.dst=address
#ip.src='192.168.100.1'


tcp=TCP()
tcp.dport=port
tcp.sport=1234
tcp.flags='S'


a=sr1(ip/tcp)
#print(a.summary())
#temp=a.summary()

if a[1].flags.value==18:
	print("port is opened")
else:
	print("port is closed")





