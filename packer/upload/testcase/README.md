# SECT Bachelor Project: Honeypot - Attack Testcase
Some attack testcase:
- Portscan
- Brute Force
- DOS: Flood and Smurf
- Malware [in progress]

## Intro
To run the testcase, we need to connect with our **attacker-container**.
For that we can run `docker exec -it attacker /bin/bash`
All attack demonstrations are located in the folder `/testcase/`
Now we can choose which attack to demonstrate:

### Portscan
Portscan is a scanning method to find out which ports are open on the target system. There are 2 kinds of portscan:
1. Simple portscan: `./portscan/portscan.sh`
2. Advanced portscan: `./portscan/portscan_advanced.sh`
Notes: Advanced portscan scan every possible TCP port and it is more aggresive.

### Brute Force
All possible usernames are stored in `usernames.txt` and all possible passwords in `passwords.txt`. The script tries all username-password combinations and if a working combination is found, it will be stored separately.
To run simply run `./bruteforce/bruteforce.sh`

### DOS (Denial of Service)
DoS Testcase consist of 2 different method: flooding and smurf.
1. To run flooding attack run `./DOS/flood/flood.sh`
2. To run smurf attack run `./DOS/smurf/smurf.sh`

### Malware (upcoming)
