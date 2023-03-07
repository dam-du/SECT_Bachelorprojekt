#! /bin/bash

# packer build docker images
cd packer/
packer init .
packer fmt .
packer build .

# run docker container
cd ..
mkdir -p honeypot_logs
docker run \
 -d --privileged=true --name honeypot_container -it \
 --mount type=bind,source="$(pwd)"/modules,target=/home/cowrie/modules \
 --mount type=bind,source="$(pwd)"/honeypot_logs,target=/home/cowrie/cowrie/var/log/cowrie \
 --privileged --expose 80 --expose 2222 honeypot_image:latest
docker run -d --name attacker_container -it --privileged attacker_image:latest
docker run -d --name attacker_container_1 -it --privileged attacker_image:latest
docker run --name simple-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx

# PRINTOUT IP of the honeypots
echo "honeypot: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' honeypot_container && \
echo "1st attacker: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' attacker_container && \
echo "2nd attacker: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' attacker_container_1 && \
echo "simple-nginx: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' simple-nginx
