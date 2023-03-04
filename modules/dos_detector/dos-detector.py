#!/usr/bin/env python3

from datetime import datetime
from scapy.all import *
import os.path
import socket   

def handler(packet):
    msg = ''
    datetime_today = datetime.today()
    log_time = datetime_today.strftime('%Y-%m-%dT%H:%M:%S')
    dt = datetime_today.strftime('%Y-%m-%d %H:%M:%S')
    host_name=socket.gethostname()   
    host_ip=socket.gethostbyname(host_name)
    packet_summary = packet.summary() + " " + dt
    if packet.haslayer(ICMP) or "icmp" in packet_summary:
        if packet.getlayer(IP).src != host_ip and "echo-reply" in packet_summary:
            msg = log_time + " [DOS]: Smurf from {} (spoofed).".format(packet.getlayer(IP).src)
            append_to_log(msg)
            append_to_file(packet_summary, "/home/cowrie/modules/dos_detector/data/data_smurf")
        else:
            if(is_icmp_flood(packet_summary)):
                msg = log_time + " [DOS]: ICMP-Flood from {}.".format(packet.getlayer(IP).src)
            append_to_log(msg)
            append_to_file(packet_summary, "/home/cowrie/modules/dos_detector/data/data_ping_icmp")
    elif packet.haslayer(TCP) or "tcp" in packet_summary:
        if packet.haslayer(Raw) and not host_ip+":2222" in packet_summary:
            if(is_tcp_flood(packet_summary)):
                msg = log_time + " [DOS]: TCP-Flood from {}.".format(packet.getlayer(IP).src)
                append_to_log(msg)
            append_to_file(packet_summary, "/home/cowrie/modules/dos_detector/data/data_ping_tcp")
    else:
        append_to_file(packet_summary, "/home/cowrie/modules/dos_detector/data/unclassified")

def append_to_file(msg, file_name):
    with open(file_name, "a+") as f:
        f.write(msg+"\n")

def append_to_log(msg):
    if not is_alerted(msg):
        file_log = '/home/cowrie/cowrie/var/log/cowrie/honeypot.log'
        file_alert = '/home/cowrie/modules/dos_detector/data/data_alerted'
        append_to_file(msg, file_log)
        append_to_file(msg, file_alert)
    else:
        pass

def is_alerted(packet_summary):
    filepath = "/home/cowrie/modules/dos_detector/data/data_alerted"
    is_exist = os.path.exists(filepath)
    if is_exist:
        with open(filepath) as f:
            for line in f:
                if packet_summary in line:
                    return True
        return False
    else:
        return False

def is_icmp_flood(packet_summary):
    counter = 0
    filepath = "/home/cowrie/modules/dos_detector/data/data_ping_icmp"
    is_exist = os.path.exists(filepath)
    if is_exist:
        with open(filepath) as f:
            for line_raw in f:
                line_edited = remove_unsused(line_raw).strip().split(" ")
                packet_edited = remove_unsused(packet_summary).split(" ")
                if(packet_edited[0]==line_edited[0]):
                    dt = line_edited[len(line_edited)-2] + " " + line_edited[len(line_edited)-1]
                    date_time_obj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
                    delta = int((datetime.today()-date_time_obj).total_seconds())
                    if delta == 0:
                        counter += 1
        if counter > 4:
            return True
        else:
            return False 
    else:
        return False

def is_tcp_flood(packet_summary):
    counter = 0
    dt_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    filepath = "/home/cowrie/modules/dos_detector/data/data_ping_tcp"
    is_exist = os.path.exists(filepath)
    if is_exist:
        with open(filepath) as f:
            for line_raw in f:
                line_edited = remove_unsused(line_raw).strip().split(" ")
                packet_edited = remove_unsused(packet_summary).split(" ")
                if ":" in packet_edited:
                    tmp = packet_edited[0].split(":")
                    src_pkt = tmp[0]
                else:
                    src_pkt = packet_edited[0]
                if ":" in line_edited:
                    tmp = line_edited[0].split(":")
                    src_line = tmp[0]
                else:
                    src_line = packet_edited[0]
                if(src_pkt == src_line):
                    dt = line_edited[len(line_edited)-2] + " " + line_edited[len(line_edited)-1]
                    date_time_obj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
                    delta = int((datetime.today()-date_time_obj).total_seconds())
                    if delta == 0:
                        counter += 1
        if counter > 0:
            return True
        else:
            return False 
    else:
        return False

def remove_unsused(line_raw):
    return remove_Ether(line_raw)

def remove_Ether(line_with_ether):
    return remove_IP(line_with_ether.replace("Ether / ", ""))

def remove_IP(line_with_ip):
    return remove_ICMP(line_with_ip.replace("IP / ", ""))

def remove_ICMP(line_with_ip):
    return remove_TCP(line_with_ip.replace("ICMP", ""))

def remove_TCP(line_with_ip):
    return remove_symbol(line_with_ip.replace("TCP", ""))

def remove_symbol(line_with_symbol):
    return line_with_symbol.replace(" >", "")

if __name__ == "__main__":
    sniff(iface="eth0", prn=handler, store=0)
