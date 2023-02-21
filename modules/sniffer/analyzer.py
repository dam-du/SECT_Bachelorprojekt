import socket   

def main():
    host_name=socket.gethostname()   
    host_ip=socket.gethostbyname(host_name)
    filepath = "temp"
    with open(filepath) as fp:
       for line_raw in fp:
           line_edited = remove_unsused(line_raw).strip().split(" ")
           print(line_edited)
           analyzer(line_edited, host_ip)

def analyzer(line_edited, host_ip):
    if line_edited[0] == "ICMP":
        if line_edited[2] == host_ip:
            if line_edited[3] == 'echo-reply':
                print("DOS-Detector: Smurf from", line_edited[1], "detected")
        elif line_edited[6] == "Raw":
            print("Ping from", line_edited[1], "received")
    elif line_edited[0] == "TCP":
        if "S" in line_edited:
            if "Raw" in line_edited:
                ip_and_port = line_edited[1].split(":")
                print("DOS-Detector: Synflood from", ip_and_port[0], "detected")
    if "frag" in line_edited:
        print("DOS-Detector: Pingflood from", line_edited[0], "detected")

def remove_unsused(line_raw):
    return remove_Ether(line_raw)

def remove_Ether(line_with_ether):
    return remove_IP(line_with_ether.replace("Ether / ", ""))

def remove_IP(line_with_ip):
    return remove_symbol(line_with_ip.replace("IP / ", ""))

def remove_symbol(line_with_symbol):
    return line_with_symbol.replace(" >", "")

def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
    for word in words:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1

if __name__ == '__main__':
    main()