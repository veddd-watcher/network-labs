# Subnet Calculator

A small Python command-line tool that takes a network in CIDR notation and prints its key details.

## What it does
Given a network such as 192.168.1.0/26, it shows:
- Network address
- Netmask
- Broadcast address
- Number of usable hosts
- First and last usable host

## How to run
Requires Python 3 (uses only the standard ipaddress module).


python3 subnet_calc.py
Enter network (e.g. 192.168.1.0/26): 192.168.1.0/26


## Example output

Network:    192.168.1.0
Netmask:    255.255.255.192
Broadcast:  192.168.1.63
Usable:     62
First host: 192.168.1.1
Last host:  192.168.1.62


## What I learned
- The number after the slash is how many bits belong to the network. The remaining host bits give 2^bits addresses.
- Two addresses are reserved in every subnet: the network address and the broadcast address, so usable hosts = 2^bits - 2.
- A bigger slash number means a smaller network. A /24 splits into four /26 networks.
- To size a subnet, pick the smallest one that fits the number of devices. For 50 devices, that's a /26 (62 usable).
