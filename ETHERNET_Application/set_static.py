import os

def set_static_ip(interface, address, netmask, gateway, dns_servers):
    """
    Configures static IP using systemd-networkd by creating a .network file in /etc/systemd/network/
    
    :param interface: Interface name (e.g., 'eth0')
    :param address: Static IP address (e.g., '192.168.1.100')
    :param netmask: Netmask in decimal (e.g., '255.255.255.0')
    :param gateway: Default gateway (e.g., '192.168.1.1')
    :param dns_servers: List of DNS servers (e.g., ['8.8.8.8', '1.1.1.1'])
    """

    # Convert netmask to CIDR
    def netmask_to_cidr(mask):
        return sum([bin(int(x)).count('1') for x in mask.split('.')])

    cidr = netmask_to_cidr(netmask)
    ip_cidr = f"{address}/{cidr}"
    dns_line = " ".join(dns_servers)

    # Prepare .network file content
    network_config = f"""[Match]
    Name={interface}

    [Network]
    Address={ip_cidr}
    Gateway={gateway}
    DNS={dns_line}
"""

    # File path
    file_path = f"/etc/systemd/network/{interface}.network"

    try:
        # Backup any existing config
        if os.path.exists(file_path):
            os.system(f"sudo cp {file_path} {file_path}.bak")

        # Write the new .network config
        with open(file_path, "w") as f:
            f.write(network_config)

        print(f"Static IP configuration written to {file_path}")

        # Enable and restart systemd-networkd
        os.system("sudo systemctl enable systemd-networkd")
        os.system("sudo systemctl restart systemd-networkd")
        print("static ip set success.")

    except Exception as e:
        print(f"Failed to configure static IP using systemd: {e}")
