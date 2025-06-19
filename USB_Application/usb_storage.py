import os
#-----------------------------------------------------------------------
def test_mass_storage(mount_path):
    """
        Function used to write and read to and from the usb device.
        :return: None.
        """
    test_file = os.path.join(mount_path, "test_usb_rw.txt")
    test_data = "USB Mass Storage Test - Hello, world!"
    #---------------------------------------------------------
    #>>Writing to the usb device
    #---------------------------------------------------------
    try:
        with open(test_file, "w", encoding="utf-8") as f:
            f.write(test_data)
        print("[WRITE] Data written successfully.")
    except Exception as e:
        print(f"[ERROR] Writing to USB failed: {e}")
        return
    #---------------------------------------------------------
    #>>Reading from the usb device
    #---------------------------------------------------------
    try:
        with open(test_file, "r", encoding="utf-8") as f:
            data = f.read()
        print(f"[READ] Data read: {data}")
        if data == test_data:
            print("[SUCCESS] Read/Write test passed!")
        else:
            print("[FAIL] Data mismatch.")
    except Exception as e:
        print(f"[ERROR] Reading from USB failed: {e}")
    #---------------------------------------------------------
    #>>remove that test file from the device
    #---------------------------------------------------------
    try:
        os.remove(test_file)
        print("[CLEANUP] Test file deleted.")
    except Exception as e:
        print(f"[ERROR] Cleanup failed: {e}")
