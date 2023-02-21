#! /bin/bash
python3 /home/cowrie/modules/portscan_detector/portscans.py -d -f "/home/cowrie/cowrie/var/log/cowrie/cowrie.log"
source /home/cowrie/cowrie/cowrie-env/bin/activate
python3 /home/cowrie/module/dos_detector/dos-detector.py &
tail -f /home/cowrie/cowrie/var/log/cowrie/cowrie.log
