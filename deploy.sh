#! /bin/bash

# packer build docker images
cd packer/
packer init .
packer fmt .
packer build .

# run container
docker run -d --privileged=true --name honeypot_container -it \
  --mount type=bind,source="$(pwd)"/modules,target=/home/cowrie/modules \
  --mount type=bind,source="$(pwd)"/honeypot_logs,target=/home/cowrie/cowrie/var/log/cowrie \
  -p 1024-49151:1024-49151 honeypot_image:latest

# PRINTOUT IP of the honeypots
echo "honeypot: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' honeypot_container
