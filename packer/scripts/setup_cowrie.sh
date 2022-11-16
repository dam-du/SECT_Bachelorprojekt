#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

cd /home/cowrie
git clone http://github.com/cowrie/cowrie
cd cowrie
virtualenv --python=python3 cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install --upgrade -r requirements.txt

mv /home/cowrie/honeypot/cowrie.cfg /home/cowrie/cowrie/etc/
mv /home/cowrie/honeypot/cowrie.sh /
chown -R cowrie:cowrie /home/cowrie/cowrie
