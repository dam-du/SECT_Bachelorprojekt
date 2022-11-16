#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

cd /home/cowrie/cowrie
source cowrie-env/bin/activate
bin/cowrie start
