#!/opt/bin/python

#sends a dhcp request with a mud url in option 161
#this is to masquarade as an IoT device following RFC 8520
#unit test for NRT Lab router script

#Written by Gabriel Brown

from scapy.all import *
import time

conf.checkIPaddr = False

fam,hw = get_if_raw_hwaddr(conf.iface)

dhcp_discover = Ether(dst="ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0",dst="255.255.255.255")/UDP(sport=68,dport=67)/BOOTP(chaddr=hw)/DHCP(options=[("message-type","discover"), (161,"http://192.168.2.118/Manufacture/AmazonEcho.json"),"end"])
#wireshark(dhcp_discover)
#print(dhcp_discover.show())
ans, unans = srp1(dhcp_discover, multi=True)
