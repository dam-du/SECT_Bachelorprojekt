#! /bin/bash
# -p0- asks Nmap to scan every possible TCP port
# -v asks Nmap to be verbose about it
# -A enables aggressive tests such as remote OS detection, service/version detection, and the Nmap Scripting Engine (NSE)
# Finally, -T4 enables a more aggressive timing policy to speed up the scan.
nmap -p0- -v -A -T4 172.17.0.2
