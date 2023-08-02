import os
import time
from scapy.all import sniff

def packet_summary(packet):
    summary = f"{packet.summary()}"
    log_dir = "/home/iotac/src/SECT_Bachelorprojekt/honeypot_logs/raw"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_filename = os.path.join(log_dir, time.strftime("%Y-%m-%d") + "-sniffed.log")
    with open(log_filename, "a") as log_file:
        log_file.write(summary + "\n")

def sniff_network_traffic():
    print("Starte das Sniffing des Netzwerkverkehrs. Drücke 'Ctrl + C' zum Beenden.")
    try:
        sniff(prn=packet_summary, iface="eth0")
    except KeyboardInterrupt:
        print("Sniffing beendet.")

if __name__ == "__main__":
    sniff_network_traffic()
