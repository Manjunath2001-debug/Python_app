import subprocess
def set_dynamic_ip(interface):
    """
        Function to set the ip dyanamic.
        
        :param interface: It specifies the ethernet interface.
        :return: None.
        """
    try:
        # Release any previous lease
        subprocess.run(["sudo", "dhclient", "-r", interface], check=True)

        # Bring interface up (optional)
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)

        # Request IP via DHCP with timeout
        subprocess.run(["sudo", "dhclient", interface], check=True, timeout=10)

        print(f"Dynamic IP configured successfully on {interface}.")
    except subprocess.TimeoutExpired:
        print(f"DHCP request timed out on {interface}. No DHCP server?")
    except subprocess.CalledProcessError as e:
        print(f"Error setting dynamic IP: {e}")
