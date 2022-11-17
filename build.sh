#! /bin/bash

# packer build docker images
cd packer/
packer init .
packer fmt .
packer build .

# run docker container
cd ..
docker run \
 -d --privileged=true --name honeypot_container -it \
 --mount type=bind,source="$(pwd)"/modules,target=/home/cowrie/modules \
 --privileged --expose 80 --expose 2222 honeypot_image:latest
docker run -d --name attacker_container -it --privileged attacker_image:latest
docker run --name simple-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx

# PRINTOUT IP of the honeypots
echo "honeypot: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' honeypot_container && \
echo "attacker: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' attacker_container && \
echo "simple-nginx: " && docker inspect -f '{{ range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' simple-nginx
