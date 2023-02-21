#!/usr/bin/env python3

from datetime import date
from scapy.all import *

def handler(packet):
    filename = date.today().strftime('%Y-%m-%d')
    myfile = open(filename,'a+')
    myfile.write(packet.summary()+"\n")

if __name__ == "__main__":
    sniff(iface="eth0", prn=handler, store=0)