#! /bin/bash
source /home/cowrie/cowrie/cowrie-env/bin/activate
python3 /home/cowrie/modules/dos_detector/test.py
tail -f /home/cowrie/cowrie/var/log/cowrie/cowrie.log
