#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

cd /testcase/
source /testcase/attacker-env/bin/activate
pip install paramiko colorama
cd bruteforce
python3 bruteforce.py 172.17.0.2 -u usernames.txt -P passwords.txt
