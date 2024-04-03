
# + id="AXROaNNEtx0g"
# !pip install scapy matplotlib

# + id="wT2owBsLt5ek"
from scapy.all import IP, ICMP, sr, traceroute

# Define the target host
target_host = ["bing.com", "google.com", "duckduckgo.com"]

# Perform the traceroute
result, _ = traceroute(target_host, maxttl=5)

# Display the results
result.show()


# + id="RX8taOgugq_M"
from scapy.all import sniff

# Lists to store packet sizes and timestamps
packet_sizes = []
timestamps = []

#Handle packets and get the necessary data
def packet_handler(packet):
  print(packet)
  packet_sizes.append(len(packet))
  timestamps.append(packet.time)

# Start packet sniffing on the default network interface
sniff(prn=packet_handler, count=100)

# + id="WEUyMfhFUJxQ"
import matplotlib.pyplot as plt

# Create a plot
plt.figure(figsize=(16, 8))
plt.plot(timestamps, packet_sizes, marker='o')
plt.xlabel("Time")
plt.ylabel("Packet Size")
plt.title("Packet Size over Time")
plt.grid(True)
plt.show()

# + id="kQIJfuJE2Wjd"
from scapy.all import sniff
from scapy.layers.inet import IP
import matplotlib.pyplot as plt

# Lists to store packet sizes and timestamps
packet_sizes = []
timestamps = []

def packet_handler(packet):
  print(packet)
  packet_sizes.append(len(packet))
  timestamps.append(packet.time)

# Start packet sniffing on the default network interface
sniff(prn=packet_handler, filter="ip", count=100)

# Create a plot
plt.figure(figsize=(16, 8))
plt.plot(timestamps, packet_sizes, marker='o')
plt.xlabel("Time")
plt.ylabel("Packet Size")
plt.title("Packet Size over Time")
plt.grid(True)
plt.show()


# + id="fj9QwdCZXewJ"
# !pip install netifaces

# + id="hir370m3XjVE"
import netifaces

def generate_routing_table():
    routing_table = []
    for interface in netifaces.interfaces():
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for entry in addresses[netifaces.AF_INET]:
                if 'netmask' in entry and 'addr' in entry:
                    routing_entry = {
                        'interface': interface,
                        'destination': entry['addr'],
                        'netmask': entry['netmask']
                    }
                    routing_table.append(routing_entry)
    return routing_table

routing_table = generate_routing_table()
for entry in routing_table:
        print(f"Interface: {entry['interface']}")
        print(f"Destination: {entry['destination']}")
        print(f"Netmask: {entry['netmask']}")
        print("-" * 30)

