#!/bin/bash

cd /home/iotac/src/SECT_Bachelorprojekt/honeypot_logs
cp -r * /home/iotac/src/BA
cd /home/iotac/src/BA
git add .
git commit -m "update"
git push
