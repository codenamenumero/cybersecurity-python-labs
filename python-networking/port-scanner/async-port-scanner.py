import asyncio
import json
import time
import argparse

# ----------------------
# CLI ARGUMENTS
# ----------------------
parser = argparse.ArgumentParser(description="AsyncIO Port Scanner")
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
# GLOBALS
# ----------------------
open_ports = []

# Limit concurrent connections
semaphore = asyncio.Semaphore(100)

# ----------------------
# SERVICE IDENTIFICATION
# ----------------------
def get_service(port):
    return COMMON_SERVICES.get(port, "Unknown Service")

# ----------------------
# BANNER GRABBER
# ----------------------
async def grab_banner(reader, writer, port):
    try:
        # HTTP-aware probing
        if port in [80, 8080, 8000, 8443, 5000]:
            request = (
                f"GET / HTTP/1.1\r\n"
                f"Host: {target}\r\n"
                f"Connection: close\r\n\r\n"
            )

            writer.write(request.encode())
            await writer.drain()

        data = await asyncio.wait_for(
            reader.read(1024),
            timeout=1
        )

        if not data:
            return None

        banner = data.decode(errors="ignore").strip()

        # Only keep first line for cleaner output
        return banner.splitlines()[0] if banner else None

    except:
        return None

# ----------------------
# PORT SCANNER
# ----------------------
async def scan_port(port):
    async with semaphore:

        try:
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(target, port),
                timeout=2
            )

            service = get_service(port)

            banner = await grab_banner(
                reader,
                writer,
                port
            )

            result = {
                "port": port,
                "status": "open",
                "service": service,
                "banner": banner if banner else ""
            }

            open_ports.append(result)

            print(
                f"[+] [{port}] OPEN "
                f"({service}) "
                f"- Banner: {banner if banner else 'No banner'}"
            )

            writer.close()
            await writer.wait_closed()

        except (
            ConnectionRefusedError,
            TimeoutError,
            OSError,
            asyncio.TimeoutError
        ):
            pass

# ----------------------
# MAIN
# ----------------------
async def main():
    print(f"\nScanning {target}")
    print(f"Port Range: {start_port}-{end_port}\n")

    start_time = time.time()

    ports = range(start_port, end_port + 1)

    await asyncio.gather(
        *(scan_port(port) for port in ports)
    )

    duration = round(time.time() - start_time, 2)

    # ----------------------
    # SAVE RESULTS
    # ----------------------
    output_file = f"scan_{target.replace('.', '_')}.json"

    with open(output_file, "w") as f:
        json.dump(
            {
                "target": target,
                "scan_range": f"{start_port}-{end_port}",
                "duration_seconds": duration,
                "total_open_ports": len(open_ports),
                "open_ports": sorted(
                    open_ports,
                    key=lambda x: x["port"]
                )
            },
            f,
            indent=4
        )

    # ----------------------
    # SUMMARY
    # ----------------------
    print("\n" + "=" * 50)
    print("SCAN COMPLETE")
    print("=" * 50)
    print(f"Target: {target}")
    print(f"Duration: {duration} seconds")
    print(f"Open Ports Found: {len(open_ports)}")
    print(f"Results Saved: {output_file}")

    if open_ports:
        print("\nOpen Ports:")
        for port_info in sorted(open_ports, key=lambda x: x["port"]):
            print(
                f"  {port_info['port']:>5} "
                f"({port_info['service']})"
            )
    else:
        print("\nNo open ports found.")

# ----------------------
# ENTRY POINT
# ----------------------
if __name__ == "__main__":
    asyncio.run(main())