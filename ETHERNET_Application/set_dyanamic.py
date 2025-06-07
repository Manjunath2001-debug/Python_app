import os

def set_dynamic_ip(interface):
    """
    Configures DHCP (dynamic IP) for a network interface in /etc/network/interfaces.

    :param interface: Network interface name (e.g., 'eth0')
    """

    dhcp_config = f"""auto {interface}
    iface {interface} inet dhcp
    """

    try:
        os.system("sudo cp /etc/network/interfaces /etc/network/interfaces.bak")

        with open("/etc/network/interfaces", "w") as f:
            f.write(dhcp_config)

        print("DHCP configuration written successfully.")

        os.system("sudo systemctl restart networking")
        print("Networking service restarted.")
    except Exception as e:
        print(f"Failed to configure DHCP: {e}")
