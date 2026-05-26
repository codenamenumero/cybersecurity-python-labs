import socket
import json
import time
import argparse
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

lock = Lock()
open_ports = []

# ----------------------
# CLI ARGUMENTS
# ----------------------
parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
parser.add_argument("target", help="Target IP address")
parser.add_argument("--start", type=int, default=1, help="Start port")
parser.add_argument("--end", type=int, default=1000, help="End port")
args = parser.parse_args()


target = args.target
start_port = args.start
end_port = args.end


# ----------------------
# SERVICE MAP
# ----------------------
COMMON_SERVICES = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5000: "Flask/Development Server",
    5900: "VNC",
    6379: "Redis",
    7000: "Dev Services",
    8000: "HTTP Alternate",
    8080: "HTTP Alternate",
    8443: "HTTPS Alternate"
}


# ----------------------
# SERVICE IDENTIFICATION
# ----------------------
def get_service(port):
    return COMMON_SERVICES.get(port, "Unknown Service")


# ----------------------
# HTTP BANNER GRABBER
# ----------------------
def grab_banner(sock):
    try:
        sock.settimeout(0.5)
        request = b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n"
        sock.sendall(request)
        response = sock.recv(1024).decode(errors='ignore')
        return response.split("\r\n")[0]  # first HTTP response line
    except:
        return None

# ----------------------
# GENERIC BANNER GRABBER
# ----------------------


def grab_generic_banner(sock):
    try:
        sock.settimeout(0.5)
        return sock.recv(1024).decode(errors='ignore').strip()
    except:
        return None


# ----------------------
# SCAN FUNCTION
# ----------------------
def scan_port(port):
    

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        service = get_service(port)

        banner = None

        # HTTP-aware detection
        if port in [80, 8080, 8000, 8443, 5000]:
            banner = grab_banner(sock)
        else:
            banner = grab_generic_banner(sock)

        data = {
            "target": target,
            "port": port,
            "service": service,
            "banner": banner if banner else "",
            "status": "open"
        }

        if banner:
            print(
                f"[+] [{port}] is open on {target} ({service}) - Banner: {banner}")
        else:
            print(
                f"[+] [{port}] is open on {target} ({service}) --| No banner retrieved)")

        with lock:
            open_ports.append(data)

    sock.close()


# ----------------------
# MAIN EXECUTION
# ----------------------
print(f"\nScanning {target}...")

start_time = time.time()
ports = range(start_port, end_port + 1)

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, ports)

end_time = time.time()
duration = round(end_time - start_time, 2)



# ----------------------
# SAVE TO JSON
# ----------------------
output_file = f"scan_{target.replace('.', '_')}.json"
with open(output_file, "w") as f:
    json.dump({
        "target": target,
        "scan_range": f"{start_port}-{end_port}",
        "duration_seconds": duration,
        "open_ports": open_ports,
    }, f, indent=4)

# ----------------------
# SUMMARY
# ----------------------
print("\nScan complete.")
print(f"Time taken: {duration} seconds")
print(f"Open ports saved to: {output_file}")

if not open_ports:
    print(f"[-] No open ports found on {target}.")
else:
    print(f"\n[+] Total open ports found on {target}: {len(open_ports)}")
