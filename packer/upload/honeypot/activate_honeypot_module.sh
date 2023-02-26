#! /bin/bash
python3 /home/cowrie/modules/portscan_detector/portscans.py -d -f "/home/cowrie/cowrie/var/log/cowrie/cowrie.log"
source /home/cowrie/cowrie/cowrie-env/bin/activate
mkdir -p /home/cowrie/modules/dos_detector/data 
python3 /home/cowrie/modules/dos_detector/dos-detector.py &
tail -f /home/cowrie/cowrie/var/log/cowrie/cowrie.log
