from scapy.all import *

print("SNIFFING PACKETS")


def print_pkt(pkt):
    print("Source IP:", pkt[IP].src)
    print("Destination IP:", pkt[IP].dst)
    print("Protocol:", pkt[IP].proto)
    print("\n")


pkt = sniff(filter='icmp', prn=print_pkt)
