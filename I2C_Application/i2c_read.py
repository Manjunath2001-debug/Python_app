def i2c_read(bus, addr, reg):
    """
        Function to read the data in I2C.
        
        :param bus: I2C bus object returned by SMBus.
        :param addr: I2C address of the device (e.g., 0x48)
        :param reg: Register address to read from device (e.g., 0x00)
        :return: integer value read from that device register or None.
        """
    try:
        value = bus.read_byte_data(addr, reg)
        print(f"Read {value} from register {reg}")
        return value
    except Exception as e:
        print(f"I2C read error: {e}")
        return None