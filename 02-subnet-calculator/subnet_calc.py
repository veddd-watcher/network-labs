import ipaddress

cidr = input("Enter network (e.g. 192.168.1.0/26): ")
n = ipaddress.ip_network(cidr, strict=False)
hosts = list(n.hosts())

print("Network:   ", n.network_address)
print("Netmask:   ", n.netmask)
print("Broadcast: ", n.broadcast_address)
print("Usable:    ", len(hosts))
print("First host:", hosts[0])
print("Last host: ", hosts[-1])
