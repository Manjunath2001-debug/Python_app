import os

def set_static_ip(interface, address, netmask, gateway, dns_servers):
    """
    Function to Configures a static IP address in /etc/network/interfaces and updates /etc/resolv.conf.

    :param interface: Network interface name (e.g., 'eth0')
    :param address: Static IP address (e.g., '192.168.1.100')
    :param netmask: Subnet mask (e.g., '255.255.255.0')
    :param gateway: Default gateway (e.g., '192.168.1.1')
    :param dns_servers: List of DNS servers (e.g., ['8.8.8.8', '8.8.8.8'])
    """

    interfaces_config = f"""auto {interface}
iface {interface} inet static
    address {address}
    netmask {netmask}
    gateway {gateway}
    dns-nameservers {' '.join(dns_servers)}
"""

    resolv_conf = "\n".join([f"nameserver {dns}" for dns in dns_servers])

    try:
        os.system("sudo cp /etc/network/interfaces /etc/network/interfaces.bak")

        with open("/etc/network/interfaces", "w") as f:
            f.write(interfaces_config)

        with open("/etc/resolv.conf", "w") as f:
            f.write(resolv_conf + "\n")

        print("Static IP configuration written successfully")

        os.system("sudo systemctl restart networking")
        print("Networking service restarted.")

    except Exception as e:
        print(f"Failed to configure static IP: {e}")


