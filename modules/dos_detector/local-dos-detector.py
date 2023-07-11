#!/usr/bin/env python3

from datetime import datetime
from scapy.all import *
import os.path
import socket   

def handler(packet):
    msg = ''
    datetime_today = datetime.today()
    current_date_string = datetime_today.strftime("%Y-%m-%d")
    log_time = datetime_today.strftime('%Y-%m-%dT%H:%M:%S')
    dt = datetime_today.strftime('%Y-%m-%d %H:%M:%S')
    host_name=socket.gethostname()   
    host_ip=socket.gethostbyname(host_name)
    packet_summary = packet.summary() + " " + dt

    if packet.haslayer(ICMP) or "icmp" in packet_summary:
        if packet.getlayer(IP).src != host_ip and "echo-reply" in packet_summary:
            msg = log_time + " [DOS]: Smurf from {} (spoofed).".format(packet.getlayer(IP).src)
            append_to_log(msg)
            data_file_name = "/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/dos/smurf.log"
            append_to_file(packet_summary, data_file_name)
        else:
            if(is_icmp_flood(packet_summary, datetime_today, host_ip)):
                msg = log_time + " [DOS]: ICMP-Flood from {}.".format(packet.getlayer(IP).src)
                append_to_log(msg)
            data_file_name = "/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/dos/icmpflood.log"
            append_to_file(packet_summary, data_file_name)
    elif packet.haslayer(TCP) or "tcp" in packet_summary:
        if packet.haslayer(Raw) and not host_ip+":2222" in packet_summary and not 'PA / Raw' in packet_summary:
            if not 'A / Raw' in packet_summary:
                if(is_tcp_flood(packet_summary)):
                    msg = log_time + " [DOS]: TCP-Flood from {}.".format(packet.getlayer(IP).src)
                    append_to_log(msg)
            data_file_name = "/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/dos/tcpflood.log"
            append_to_file(packet_summary, data_file_name)
    else:
        data_file_name = "/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/unclassified/unclassified.log"
        append_to_file(packet_summary, data_file_name)

def append_to_file(msg, file_name):
    with open(file_name, "a+") as f:
        f.write(msg+"\n")

def append_to_log(msg):
    if not is_alerted(msg):
        datetime_today = datetime.today()
        current_date_string = datetime_today.strftime("%Y-%m-%d")
        file_log = '/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/honeypot_DOS.log'
        append_to_file(msg, file_log)

def count_delta(datetime_now, readed_datetime):
    if isinstance(datetime_now, str):
        dt_a = datetime.strptime(datetime_now, '%Y-%m-%d %H:%M:%S')
    else:
        dt_a = datetime_now
    dt_b = datetime.strptime(readed_datetime, '%Y-%m-%d %H:%M:%S')
    delta = int((dt_a - dt_b).total_seconds())
    return delta

def is_alerted(packet_summary):
    datetime_today = datetime.today()
    current_date_string = datetime_today.strftime("%Y-%m-%d")
    filepath = '/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/honeypot_DOS.log'
    if os.path.exists(filepath):
        with open(filepath) as f:
            for line in f:
                if packet_summary in line:
                    return True
        return False
    else:
        return False

def is_icmp_flood(packet_summary, datetime_now, host_ip):
    counter = 0
    datetime_today = datetime.today()
    current_date_string = datetime_today.strftime("%Y-%m-%d")
    filepath = "/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/dos/icmpflood.log"
    is_exist = os.path.exists(filepath)
    if is_exist:
        with open(filepath) as f:
            for line in f:
                if get_src_ip(packet_summary) == get_src_ip(line) and get_src_ip(packet_summary) != host_ip:
                    readed_datetime = get_timestamp(line)
                    delta = count_delta(datetime_now, readed_datetime)
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
    datetime_today = datetime.today()
    current_date_string = datetime_today.strftime("%Y-%m-%d")
    dt_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    filepath = "/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/dos/tcpflood.log"
    is_exist = os.path.exists(filepath)
    if is_exist:
        with open(filepath) as f:
            for line_raw in f:
                pkt_src_ip = get_src_ip(packet_summary)
                line_src_ip = get_src_ip(line_raw)
                if ":" in pkt_src_ip:
                    tmp = pkt_src_ip.split(':')
                    src_pkt = tmp[0]
                else:
                    src_pkt = pkt_src_ip
                if ":" in line_src_ip:
                    tmp = line_src_ip.split(':')
                    src_line = tmp[0]
                else:
                    src_line = line_src_ip
                if(src_pkt == src_line):
                    delta = count_delta(get_timestamp(packet_summary), get_timestamp(line_raw))
                    if delta == 0:
                        counter += 1
        if counter > 0:
            return True
        else:
            return False 
    else:
        return False

def get_timestamp(packet_summary):
    if '\n' in packet_summary:
        packet_summary = packet_summary.strip()
    packet = packet_summary.split(" ")
    date = packet[len(packet)-2]+(' ')+packet[len(packet)-1]
    return date
    
def get_src_ip(packet_summary):
    packet = packet_summary.replace('Ether ', '')
    packet = packet.replace(' IP ', '')
    packet = packet.replace(' ICMP ', '')
    packet = packet.replace(' TCP ', '')
    packet = packet.replace('/ ', '')
    packet = packet.replace('/', '')
    splitted_packet = packet.split(' ')
    return splitted_packet[0]

if __name__ == "__main__":
    sniff(iface="eth0", prn=handler, store=0)
