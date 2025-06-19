import usb.core
import usb.util
import psutil
#---------------------------------------------------------------------------------------------------------------------
usb_mount = "/mnt/usb"
#---------------------------------------------------------------------------------------------------------------------
def list_usb_devices():
    """
        Function to list the usb devices.
        :return: None.
        """
    found = False
    print("Connected USB Devices:")
    devices = usb.core.find(find_all=True)
    for device in devices:
        print(f"VID: {hex(device.idVendor)}, PID: {hex(device.idProduct)}")
        for cfg in device:
            for intf in cfg:
                if intf.bInterfaceClass == 0x08:  # Mass Storage
                    print(f" Mass Storage Device found: VID={hex(device.idVendor)}, PID={hex(device.idProduct)}")
                    found = True
    if not found:
        print("No USB Mass Storage devices found.")
    return found
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    from usb_storage import test_mass_storage

    try:
        list_usb_devices()
        print("Detecting USB...")
        test_mass_storage(usb_mount)
    except Exception as e:
        print(f"Error :{e}")
    