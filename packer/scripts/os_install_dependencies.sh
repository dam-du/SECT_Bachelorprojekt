#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y git python3-virtualenv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind virtualenv iptables net-tools
