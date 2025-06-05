def i2c_write(bus, addr, reg, data):
    """
        Function to write the data in I2C.
        
        :param bus: I2C bus object returned by SMBus.
        :param addr: I2C address of the device (e.g., 0x48)
        :param reg: Register address to read from device (e.g., 0x00)
        :param data:It specifies the input data to write.
        :return: None.
        """
    try:
        bus.write_byte_data(addr, reg, data)
        print(f"Written {data} to register {reg}")
    except Exception as e:
        print(f"I2C write error: {e}")