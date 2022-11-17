#! /bin/bash

# docker stop and delete containers
docker stop attacker_container honeypot_container simple-nginx
docker rm attacker_container honeypot_container simple-nginx
# docker delete images
docker rmi honeypot_image:latest
docker rmi attacker_image:latest
