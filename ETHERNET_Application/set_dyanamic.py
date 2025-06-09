import os

def set_dyanamic_ip(interface):
    """
    Configures DHCP for the given interface using systemd-networkd by creating
    a .network file in /etc/systemd/network/
    
    :param interface: Network interface name (e.g., 'eth0')
    """

    network_config = f"""[Match]
    Name={interface}

    [Network]
    DHCP=yes
"""

    file_path = f"/etc/systemd/network/{interface}.network"

    try:
        # Backup existing configuration if present
        if os.path.exists(file_path):
            os.system(f"sudo cp {file_path} {file_path}.bak")

        # Write DHCP configuration to the .network file
        with open(file_path, "w") as f:
            f.write(network_config)

        print(f"DHCP configuration written to {file_path}")

        # Enable and restart systemd-networkd
        os.system("sudo systemctl enable systemd-networkd")
        os.system("sudo systemctl restart systemd-networkd")
        print("systemd-networkd restarted and enabled.")

    except Exception as e:
        print(f"Failed to configure DHCP using systemd: {e}")


#-----------------------------------------------------------------------------------------------------------
# import os

# def set_dynamic_ip(interface):
#     """
#     Configures DHCP (dynamic IP) for a network interface in /etc/network/interfaces.

#     :param interface: Network interface name (e.g., 'eth0')
#     """

#     dhcp_config = f"""auto {interface}
#     iface {interface} inet dhcp
#     """

#     try:
#         os.system("sudo cp /etc/network/interfaces /etc/network/interfaces.bak")

#         with open("/etc/network/interfaces", "w") as f:
#             f.write(dhcp_config)

#         print("DHCP configuration written successfully.")

#         os.system("sudo systemctl restart networking")
#         print("Networking service restarted.")
#     except Exception as e:
#         print(f"Failed to configure DHCP: {e}")
