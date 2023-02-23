from datetime import datetime   

import socket

def main():
    is_icmp_flood()

def is_icmp_flood():
    data = dict()
    dt_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    host_name=socket.gethostname()   
    host_ip=socket.gethostbyname(host_name)
    filepath = "data_ping_icmp"
    with open(filepath) as fp:
       for line_raw in fp:
           line_edited = remove_unsused(line_raw).strip().split(" ")
           dt = line_edited[len(line_edited)-2] + " " + line_edited[len(line_edited)-1]
           date_time_obj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
           delta = int((datetime.today()-date_time_obj).total_seconds())
           print(delta)

def remove_unsused(line_raw):
    return remove_Ether(line_raw)

def remove_Ether(line_with_ether):
    return remove_IP(line_with_ether.replace("Ether / ", ""))

def remove_IP(line_with_ip):
    return remove_ICMP(line_with_ip.replace("IP / ", ""))

def remove_ICMP(line_with_ip):
    return remove_symbol(line_with_ip.replace("ICMP", ""))

def remove_symbol(line_with_symbol):
    return line_with_symbol.replace(" >", "")

if __name__ == '__main__':
    main()