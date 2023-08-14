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
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())

scan("192.168.122.1/24")


