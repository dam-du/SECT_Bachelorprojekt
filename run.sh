#! /bin/bash

docker exec -it -u cowrie honeypot_container /bin/bash
docker exec -it honeypot_container bin/bash
