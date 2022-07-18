import scapy.all as scapy
import argparse


def args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--target", dest="target", help="target ip address")

    options = parser.parse_args()

    if not options.target:
        parser.error(f"[*] please specify a target, use --help for more info.")

    return options.target


def scan(iP):
    request_packet = scapy.ARP(pdest=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_packet = broadcast_packet/request_packet
    answered_list = scapy.srp(arp_packet, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address\n---------------------------------------------------")
    for _ in answered_list:
        print(_[1].psrc + "\t\t" + _[1].hwsrc)


target = args()
scan(target)
