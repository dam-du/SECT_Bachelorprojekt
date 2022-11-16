#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

apt-get install -y nmap hping3

mkdir /testcase/ -p && cd /testcase
virtualenv --python=python3 /testcase/attacker-env
source /testcase/attacker-env/bin/activate
pip install scapy paramiko colorama
