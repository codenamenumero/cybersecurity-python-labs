import socket
import ipaddress

COMMON_PORTS = [80, 443, 22, 21, 25, 8000]

network = ipaddress.ip_network('192.168.18.0/24')

print(f"\nScanning network: {network}\n")

for ip in network.hosts():
    
    host_found = False
    
    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        
        result = sock.connect_ex((str(ip), port))
        
        if result == 0:
            print(f"Port {port} is open on {ip}\n")
            host_found = True
            sock.close()
            break
            
        sock.close()
