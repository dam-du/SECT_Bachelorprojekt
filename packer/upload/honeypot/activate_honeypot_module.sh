#! /bin/bash
python3 /home/cowrie/modules/portscan_detector/portscans.py -d -f "/home/cowrie/cowrie/var/log/cowrie/cowrie.log"
tail -f /home/cowrie/cowrie/var/log/cowrie/cowrie.log
