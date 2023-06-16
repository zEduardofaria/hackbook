# Find active hosts

```bash
nmap -sn 37.59.172.224-239
```

-   `-sn`: This option stands for "Ping Scan" and instructs nmap to perform a host discovery scan by sending ICMP echo requests (pings) to the specified IP addresses. It doesn't attempt any further port scanning or service detection.
-   `37.59.172.224-239`: This specifies a range of IP addresses to scan. In this case, it covers the IP addresses from 37.59.172.224 to 37.59.172.239.

By running this command, nmap will send ICMP echo requests to each IP address in the specified range. The tool will then report which hosts are up and responding to the ping requests. This type of scan is useful for quickly identifying active hosts on a network without performing in-depth port scans or service enumeration.