#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

sudo apt-get update
sudo apt-get install -y git python3-virtualenv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind virtualenv iptables net-tools

virtualenv --python=python3 dos-env
source dos-env/bin/activate
pip install --upgrade pip
pip install scapy
