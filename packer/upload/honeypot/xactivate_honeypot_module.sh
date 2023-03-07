#! /bin/bash
python3 /home/cowrie/modules/portscan_detector/portscans.py -d -f '/home/cowrie/cowrie/var/log/cowrie/honeypot.log'
source /home/cowrie/cowrie/cowrie-env/bin/activate
mkdir -p /home/cowrie/modules/dos_detector/data 
python3 /home/cowrie/modules/dos_detector/extended-dos-detector.py &
python3 /home/cowrie/modules/malware_detector/malware.py &
touch /home/cowrie/cowrie/var/log/cowrie/honeypot.log
mkdir -p /home/cowrie/cowrie/var/log/cowrie/data/recorded
tail -f /home/cowrie/cowrie/var/log/cowrie/honeypot.log
