# Lumen IDS - Network Capture Log

This log records network traffic captured for testing and evaluating Lumen IDS.

## Capture Records

| PCAP file | Scenario | Command or activity | Start time | End time | Result / observations |
|---|---|---|---|---|---|
| portscan_01.pcap | Port scan | `sudo nmap -sS 10.10.10.20`; `sudo nmap -sT -p- 10.10.10.20` | To record | To record | SYN scan initially failed with a route error. TCP connect scan found 26 open TCP ports. |
| benign_01.pcap | Benign traffic | HTTP, FTP and SSH client activity | To record | To record | Record which services responded. |
| bruteforce_ssh_01.pcap | SSH authentication test | Hydra with a three-password test list | To record | To record | Initial attempt failed during SSH host-key negotiation. Authentication attempts were not confirmed. |
| dos_01.pcap | Controlled SYN test | Bounded hping3 SYN test against TCP port 80 | To record | To record | Record actual packet count and duration. |
| web_01.pcap | Web-server scan | `nikto -h http://10.10.10.20` | To record | To record | Record scan results and errors. |

## Environment

- Traffic generator: Kali Linux
- Target: Metasploitable 2 (10.10.10.20)
- Sensor: Ubuntu Server
- Capture interface: enp0s8
- Capture tool: tcpdump
- Analysis tool: Zeek

## Notes

- Replace placeholder times with actual capture start and end times.
- Record failures and unusual observations honestly.
- Keep one PCAP per scenario.
- Avoid committing large PCAP files to Git; store them separately if needed.
