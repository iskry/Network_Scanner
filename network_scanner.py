#!/usr/bin/env python

# Importing necessary libraries/modules
import scapy.all as scapy
import optparse

# Function to get command line arguments
def getArguments():
    # Creating a parser object to handle command line arguments
    parser = optparse.OptionParser()

    # Adding option to get target IP address from the user
    parser.add_option("-t", "--target", dest="ip", help="target IP address")

    # Parsing the command line arguments and options
    (options, arguments) = parser.parse_args()

    # Check if the target IP was provided, if not display an error message
    if not options.ip:
        parser.error("[-] Please specify an IP target")

    return options

# Function to scan the target IP for MAC addresses
def scan(ip):
    # Creating an ARP request packet to get the MAC address corresponding to the IP
    arp_request = scapy.ARP(pdst=ip)
    # Creating an Ethernet frame to transport the ARP request
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    # Sending the ARP request and getting the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # List to store details of all the clients (IP and MAC)
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

# Function to print the scan results in a formatted manner
def print_result(results_list):
    print("IP\t\t\tMac\n----------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

# Getting the target IP from command line arguments
options = getArguments()

# Scanning the target IP
scan_result = scan(options.ip)

# Printing the scan results
print_result(scan_result)

