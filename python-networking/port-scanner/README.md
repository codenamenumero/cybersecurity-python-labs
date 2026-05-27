# Async Port Scanner

A high-performance asynchronous TCP port scanner built with Python.  
This project was developed as part of a cybersecurity and networking portfolio to demonstrate practical knowledge of:

- Socket programming
- TCP networking
- Multithreading
- AsyncIO concurrency
- Service detection
- Banner grabbing
- CLI tooling
- JSON reporting

---

# Features

## Core Features
- TCP connect scanning
- Multi-threaded scanning
- AsyncIO-based scanning
- Open port detection
- LAN device scanning
- Timeout handling

## Service Detection
Identifies common services such as:
- HTTP
- HTTPS
- SSH
- MySQL
- Development servers

## Banner Grabbing
- HTTP-aware probing
- Captures service banners and responses
- Basic service fingerprinting

## Reporting
- JSON output export
- Scan timing metrics
- Clean CLI-style output

---

# Project Structure

```bash
project/
│
├── port-scanner.py          # Threaded TCP scanner
├── async-port-scanner.py    # AsyncIO scanner
├── scan_results.json        # Example scan output
└── README.md