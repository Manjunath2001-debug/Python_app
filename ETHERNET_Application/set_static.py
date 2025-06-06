import subprocess
def set_static_ip(interface, ip_address, netmask, gateway):
    """
        Function to set the ip static.
        
        :param interface: It specifies the ethernet interface.
        :param ip_address: It specifies the input ip_address.
        :param netmask: It specifies the input netmask.
        :param gateway: It specifies the gateway input.
        :return: None.
        """
    try:
        # Bring the interface down
        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        
        # Set static IP and netmask
        subprocess.run(["sudo", "ifconfig", interface, ip_address, "netmask", netmask], check=True)
        
        # Set the default gateway
        subprocess.run(["sudo", "route", "add", "default", "gw", gateway, interface], check=True)
        
        # Bring the interface up
        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print(f"Static IP {ip_address} configured successfully on {interface}.")
    except subprocess.CalledProcessError as e:
        print(f"Error setting static IP: {e}")