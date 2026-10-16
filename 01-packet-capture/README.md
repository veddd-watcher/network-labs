# Packet Capture: Ping to Google

Captured an ICMP ping from my Mac to google.com with Wireshark to see how a local host reaches a remote one.

## Captured values
- Source MAC: de:7b:02:29:90:cd (my Mac, Wi-Fi)
- Destination MAC: 98:9d:b2:31:1b:51 (my home router)
- Source IP: 192.168.1.13 (my Mac)
- Destination IP: 142.251.43.46 (Google)


<img width="1710" height="1107" alt="capture" src="https://github.com/user-attachments/assets/9843b847-d4b4-486d-8d31-5e484d9c34da" />
- 
## What this shows
Google isn't on my local network, so my Mac sends the frame to its default gateway (the router). The destination IP stays Google's, while the destination MAC is the router's, since the router is the next hop. At each hop, the MAC addresses are rewritten and the destination IP stays the same.

## Verification
arp -a shows 192.168.1.1 at 98:9d:b2:31:1b:51, matching the destination MAC in the capture.

## Tools
Wireshark 4.6.9, macOS Terminal (ping, arp)
