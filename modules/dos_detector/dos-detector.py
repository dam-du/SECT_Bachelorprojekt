#!/usr/bin/env python3

from datetime import datetime
from scapy.all import *
import socket   

def handler(packet):
    time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    host_name=socket.gethostname()   
    host_ip=socket.gethostbyname(host_name)
    packet_summary = packet.summary() + " " + time
    line_edited = remove_unsused(packet_summary).split(" ")
    analyzer(line_edited, host_ip)

def append_to_log(msg):
    with open("/home/cowrie/cowrie/var/log/cowrie/cowrie.log", "a") as myfile:
        myfile.write(msg+"\n")

def analyzer(line_edited, host_ip):
    if line_edited[0] == "ICMP":
        if line_edited[2] == host_ip:
            if line_edited[3] == 'echo-reply':
                msg = "DOS-Detector: Smurf from {} at {} {} detected".format(line_edited[1], line_edited[len(line_edited)-2], line_edited[len(line_edited)-1])
                append_to_log(msg)
        elif line_edited[6] == "Raw":
                msg = "Ping from {} at {} {} received".format(line_edited[1], line_edited[len(line_edited)-2], line_edited[len(line_edited)-1])
                append_to_log(msg)
    elif line_edited[0] == "TCP":
        if "S" in line_edited:
            if "Raw" in line_edited:
                ip_and_port = line_edited[1].split(":")
                msg = "DOS-Detector: Synflood from {} at {} {} detected".format(ip_and_port[0], line_edited[len(line_edited)-2], line_edited[len(line_edited)-1])
                append_to_log(msg)
    elif "frag" in line_edited[3]:
        msg = "DOS-Detector: Pingflood from {} at {} {} detected".format(line_edited[0], line_edited[len(line_edited)-2], line_edited[len(line_edited)-1])
        append_to_log(msg)
    else:
        msg = "unclassified {} at {} {}".format(line_edited, line_edited[len(line_edited)-2], line_edited[len(line_edited)-1])
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
