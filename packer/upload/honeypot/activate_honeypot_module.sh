#! /bin/bash
python3 /home/cowrie/modules/portscan_detector/portscans.py -d
source /home/cowrie/cowrie/cowrie-env/bin/activate

mkdir -p /home/cowrie/cowrie/var/log/cowrie/dos/
mkdir -p /home/cowrie/cowrie/var/log/cowrie/unclassified/

python3 /home/cowrie/modules/dos_detector/dos-detector.py &
python3 /home/cowrie/modules/malware_detector/malware.py &
python3 /home/cowrie/modules/utils/cleaner.py &

touch /home/cowrie/cowrie/var/log/cowrie/honeypot.log
mkdir -p /home/cowrie/cowrie/var/log/cowrie/data/recorded
tail -f /home/cowrie/cowrie/var/log/cowrie/honeypot.log
