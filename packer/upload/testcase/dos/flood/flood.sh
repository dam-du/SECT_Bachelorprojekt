#! /bin/bash
export DEBIAN_FRONTEND=noninteractive
#source: https://www.opensourceforu.com/2011/10/syn-flooding-using-scapy-and-prevention-using-iptables/

source /testcase/attacker-env/bin/activate
cd /testcase/dos/flood
python3 flood.py
