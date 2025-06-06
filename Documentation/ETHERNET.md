
# Sample application for Ethernet Interface Testing

This guide documents the process and output of testing Ethernet (`eth0`) interface with both Static and Dynamic IP configuration using Python and system commands.

---

## 📂 Project Structure

```
ETHERNET/
├── ety.py              # Main Python script to test Static/Dynamic IP and ping
├── set_static.py       # Module to configure static IP
├── set_dynamic.py      # Module to configure dynamic IP
```

---

## How It Works

### Static IP Setup

The script configures a static IP like this:

```bash
sudo ifconfig eth0 down
sudo ifconfig eth0 192.168.1.100 netmask 255.255.255.0
sudo route add default gw 192.168.1.1 eth0
sudo ifconfig eth0 up
```

### Dynamic IP Setup

It then switches to dynamic IP using DHCP:

```bash
sudo dhclient -r eth0
sudo ifconfig eth0 up
sudo dhclient eth0
```

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

| Step               | Status      |
|--------------------|-------------|
| Static IP Set      | ✅ Success  |
| Static IP Ping     | ✅ Success  |
| Dynamic IP Set     | ✅ Success  |
| Dynamic IP Ping    | ✅ Success  |

---

## Notes
- You must run the script as `sudo`
- Interface must be `eth0` or replace with actual interface
- Internet not required for `dhclient`, but DHCP server is needed


