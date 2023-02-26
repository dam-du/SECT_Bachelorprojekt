#! /bin/bash

# docker stop and delete containers
docker stop attacker_container honeypot_container simple-nginx
docker rm attacker_container honeypot_container simple-nginx

# packer build docker images
mkdir -p honeypot_logs
docker run \
 -d --privileged=true --name honeypot_container -it \
 --mount type=bind,source="$(pwd)"/modules,target=/home/cowrie/modules \
 --mount type=bind,source="$(pwd)"/honeypot_logs,target=/home/cowrie/cowrie/var/log/cowrie \
 --privileged --expose 80 --expose 2222 honeypot_image:latest
docker run -d --name attacker_container -it --privileged attacker_image:latest
docker run --name simple-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx

# PRINTOUT IP of the honeypots
echo "honeypot: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' honeypot_container && \
echo "attacker: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' attacker_container && \
echo "simple-nginx: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' simple-nginx
