
# SECT Bachelor Project: Honeypot - Testcases
### Introduction
These testcases are available inside our attacker's container
- Portscan
- Bruteforce
- DOS: Flood and Smurf
- Malware [WIP]

To run these testcases, we need to connect with our **attacker-container**.
They can be found inside `/testcase/`
  
### Portscan

Portscan is a scanning method to find out which ports are open on the target system. There are 2 kinds of portscan:
1. Simple portscan: `/testcase/portscan/portscan.sh`
2. Advanced portscan: `/testcase/portscan/portscan_advanced.sh`
![Showcase of Portscan](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/testcase_portscan.gif)

*Notes: Advanced portscan scan every possible TCP port and it is more aggresive, and it takes longer time to finish.*

### Brute Force

All possible usernames are stored in `usernames.txt` and all possible passwords in `passwords.txt`. The script tries all username-password combinations and if a working combination is found, it will be stored inside `credentials.txt`.

To test simply run `/testcase/bruteforce/bruteforce.sh`

![Showcase of Bruteforce](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/testcase_bruteforce.gif)

### DOS (Denial of Service)
The testcases consist of 2 different method: flooding and smurf.
**Flood attacks** occur when the system receives too much traffic for the server to buffer, causing them to slow down and eventually stop. Meanwhile **smurf attack** is a distributed denial-of-service attack in which large numbers of Internet Control Message Protocol packets with the intended victim's spoofed source IP are broadcast to a computer network using an IP broadcast address.
1. To test flooding attack run `/testcaste/dos/flood/flood.sh`
2. To test syn-flooding attack run `/testcaste/dos/flood/synflood.sh`
![Showcase of DOS-Flood](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/testcase_flood.gif)
3. To test smurf attack run `/testcase/dos/smurf/smurf.sh`
![Showcase of Bruteforce](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/testcase_smurf.gif)

### Malware [WIP]
