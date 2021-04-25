#Simple port scanner

import socket
import sys

target = input("IP to scan: ")
ports = input("Enter the port range to scan (ie. 5-200)")

low = int(ports.split("-")[0])
high = int(ports.split("-")[1])

print("Scanning", target, "from port", low, "to port", high)

for port in range(low, high):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print("--- PORT", port, "OPEN ---")
    else:
        print("--- PORT", port, "CLOSED ---")
    s.close()