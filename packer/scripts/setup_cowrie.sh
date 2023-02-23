#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

cd /home/cowrie
git clone http://github.com/cowrie/cowrie
cd cowrie
virtualenv --python=python3 cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install scapy
pip install --upgrade -r requirements.txt

mv /home/cowrie/cowrie.cfg /home/cowrie/cowrie/etc/
mv /home/cowrie/userdb.txt /home/cowrie/cowrie/etc/
mv /home/cowrie/cowrie.sh /
mv /home/cowrie/activate_honeypot_module.sh /

chown -R cowrie:cowrie /home/cowrie/cowrie
