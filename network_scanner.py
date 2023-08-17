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
   

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMac\n----------------------------------------------")
    for client in results_list:
        print(client)


scan_result = scan("192.168.122.1/24")
print_result(scan_result)


