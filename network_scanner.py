#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # packet below contains a combination of the broadcast and the arp_request
    arp_request_broadcast = broadcast/arp_request
    # allows us to send packets with a custom Ether part
    # will return two values (answered and unanswered) which is being assigned to variables
    # added timeout to prevent functioning hanging
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
   
    print("IP\t\t\tMac\n----------------------------------------------")
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    print(clients_list)



scan("192.168.122.1/24")


