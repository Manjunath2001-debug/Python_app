
# Sample application for Ethernet Interface Testing

This guide documents the process and output of testing Ethernet (`eth0`) interface with both Static and Dynamic IP configuration using Python and system commands.

---

## Project Structure

```
ETHERNET/
├── ety.py              # Main Python script to test Static/Dynamic IP and ping
├── set_static.py       # Module to configure static IP
├── set_dynamic.py      # Module to configure dynamic IP
```

---

## How It Works

## Function: `set_static_ip()`

### Description:
Configures a **static IP address** by editing `/etc/network/interfaces` and `/etc/resolv.conf`.

### Definition:

```python
def set_static_ip(interface, address, netmask, gateway, dns_servers):
```

### Parameters:

| Name         | Type     | Description                                 |
|--------------|----------|---------------------------------------------|
| `interface`  | `str`    | Network interface name (e.g., `"eth0"`)     |
| `address`    | `str`    | Static IP address (e.g., `"192.168.1.100"`) |
| `netmask`    | `str`    | Subnet mask (e.g., `"255.255.255.0"`)       |
| `gateway`    | `str`    | Default gateway IP (e.g., `"192.168.1.1"`)  |
| `dns_servers`| `list`   | List of DNS servers (e.g., `["8.8.8.8"]`)   |

### Behavior:
- Backs up the existing `/etc/network/interfaces`.
- Writes static IP config to `/etc/network/interfaces`.
- Writes DNS config to `/etc/resolv.conf`.
- Restarts the networking service.

---

## Function: `set_dynamic_ip()`

### Description:
Configures the interface to obtain IP dynamically via **DHCP**.

### Definition:

```python
def set_dynamic_ip(interface):
```

### Parameters:

| Name         | Type     | Description                             |
|--------------|----------|-----------------------------------------|
| `interface`  | `str`    | Network interface name (e.g., `"eth0"`) |

### Behavior:
- Backs up the existing `/etc/network/interfaces`.
- Writes DHCP config to `/etc/network/interfaces`.
- Restarts the networking service.

---

### Ping Test

It pings a public DNS server to check connectivity:

```bash
ping -c 4 8.8.8.8
```

---

## Example Output

```
Static IP 192.168.1.100 configured successfully on eth0.
Ping to 8.8.8.8 successful:
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=120 time=2062 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=120 time=1045 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=120 time=21.9 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=120 time=16.4 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss

Killed old client process
Dynamic IP configured successfully on eth0.
Ping to 8.8.8.8 successful:
64 bytes from 8.8.8.8: icmp_seq=1 ttl=120 time=19.5 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=120 time=16.9 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=120 time=15.3 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=120 time=18.3 ms

--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss
```

---

## Code works for below condition

| Step               | Status   |
|--------------------|----------|
| Static IP Set      | Success  |
| Static IP Ping     | Success  |
| Dynamic IP Set     | Success  |
| Dynamic IP Ping    | Success  |

---

## Notes
- You must run the script as `sudo`
- Interface must be `eth0` or replace with actual interface
- Internet not required for `dhclient`, but DHCP server is needed
