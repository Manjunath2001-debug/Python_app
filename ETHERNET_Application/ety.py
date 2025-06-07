#------------------------------------------------------------------------------------------------------------
#>> Sample application for ethernet to set IP_configuration static or dyanamic.
#------------------------------------------------------------------------------------------------------------
import subprocess
from set_dyanamic import set_dynamic_ip
from set_static import set_static_ip
#--------------------------------------------------------------------------------------------------------------
interface = "eth0"  
host = "8.8.8.8"   
dns_servers=["8.8.8.8", "8.8.8.8"] 
#--------------------------------------------------------------------------------------------------------------
def ping_host(host):
    """
        Function to ping host.
        
        :param host: It specifies the host.
        :return: None.
        """
    try:
        # Ping the host
        response = subprocess.run(["ping", "-c", "4", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            print(f"Ping to {host} successful:\n{response.stdout.decode()}")
        else:
            print(f"Ping to {host} failed:\n{response.stderr.decode()}")
    except Exception as e:
        print(f"Error during ping: {e}")

#---------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    try:
        while True:
            input_config = int(input("Enter the configuration type:\n1. Static IP\n2. Dynamic IP\nChoice (1 or 2): "))
            if input_config == 1:
                # Set static IP
                set_static_ip(interface, "192.168.1.100", "255.255.255.0", "192.168.1.1",dns_servers)
                ping_host(host)

            elif input_config == 2:
                # Set dynamic IP
                set_dynamic_ip(interface)
                ping_host(host)

            else:
                print("Invalid input")
    except KeyboardInterrupt:
        print("\nkeyboard interrupt")
    except Exception as e:
        print(f"/nError: {e}")
