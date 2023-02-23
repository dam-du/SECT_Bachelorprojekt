#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

apt-get update 
apt-get install python3-pip libpcap-dev -y

cd /home/cowrie/libs/dpkt/
python3 setup.py build
python3 setup.py install
cd /home/cowrie/libs/pypcap/
python3 setup.py build
python3 setup.py install

rm -rf /home/cowrie/libs
