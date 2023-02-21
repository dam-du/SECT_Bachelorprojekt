#!/usr/bin/env python3

from datetime import date
from scapy.all import *
import socket   

def handler(packet):
    host_name=socket.gethostname()   
    host_ip=socket.gethostbyname(host_name)
    packet_summary = packet.summary()
    line_edited = remove_unsused(packet_summary).split(" ")
    analyzer(line_edited, host_ip)

def append_to_log(msg):
    with open("/home/cowrie/cowrie/var/log/cowrie/cowrie.log", "a") as myfile:
        myfile.write(msg+"\n")

def analyzer(line_edited, host_ip):
    if line_edited[0] == "ICMP":
        if line_edited[2] == host_ip:
            if line_edited[3] == 'echo-reply':
                msg = "DOS-Detector: Smurf from {} detected".format(line_edited[1])
                append_to_log(msg)
        elif line_edited[6] == "Raw":
                msg = "Ping from {} received".format(line_edited[1])
                append_to_log(msg)
    elif line_edited[0] == "TCP":
        if "S" in line_edited:
            if "Raw" in line_edited:
                ip_and_port = line_edited[1].split(":")
                msg = "DOS-Detector: Synflood from {} detected".format(ip_and_port[0])
                append_to_log(msg)
    elif "frag" in line_edited[3]:
        msg = "DOS-Detector: Pingflood from {} detected".format(line_edited[0])
        append_to_log(msg)
    else:
        msg = "unclassified {}".format(line_edited)
        myfile = open("unclassified",'a+')
        myfile.write(msg+"\n")

def remove_unsused(line_raw):
    return remove_Ether(line_raw)

def remove_Ether(line_with_ether):
    return remove_IP(line_with_ether.replace("Ether / ", ""))

def remove_IP(line_with_ip):
    return remove_symbol(line_with_ip.replace("IP / ", ""))

def remove_symbol(line_with_symbol):
    return line_with_symbol.replace(" >", "")

if __name__ == "__main__":
    sniff(iface="eth0", prn=handler, store=0)
