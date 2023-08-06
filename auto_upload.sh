#!/bin/bash

# Function to run the desired script
run_script() {
    cd /home/iotac/src/SECT_Bachelorprojekt/honeypot_logs
    cp -r * /home/iotac/src/BA
    cd /home/iotac/src/BA
    git add .
    git commit -m "update"
    git push
}

while true; do
    run_script

    # Sleep for 5 hours (60 seconds/minute * 60 minutes/hour * 5 hours)
    sleep 18000
done
