#! /bin/bash

# packer build docker images
cd packer/
packer init .
packer fmt .
packer build .

# run container
docker run -d --privileged=true --name dam_honeypot -it \
  --mount type=bind,source="$(pwd)"/modules,target=/home/cowrie/modules \
  --mount type=bind,source="$(pwd)"/honeypot_logs,target=/home/cowrie/cowrie/var/log/cowrie \
  -p 1024-2500:1024-2500 honeypot_image:latest

# PRINTOUT IP of the honeypots
echo "honeypot: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' dam_honeypot
