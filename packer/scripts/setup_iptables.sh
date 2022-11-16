#! /bin/bash
export DEBIAN_FRONTEND=noninteractive

update-alternatives --set iptables /usr/sbin/iptables-legacy
