from scapy.all import *


def print_traceroute(ip):

    #creating icmp packet to send echo requests and we check ip of source after each response
    tr=IP()/ICMP()
    tr.ttl=64
    tr.dst=ip
    temp=0

    for every_ttl in range(1,256):

        tr.ttl=every_ttl
        response=sr1(tr)

        if temp==response[IP].src:
            break

        print(every_ttl, " hop away  " ,response[IP].src)
        temp=response[IP].src




server=input("enter ip you want to traceroute")
print_traceroute(server)
