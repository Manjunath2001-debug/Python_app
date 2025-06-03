def i2c_write(bus, addr, reg, data):
    """
        Function to write the data in I2C.
        
        :param bus: It specifies the.
        :param addr:
        :param reg:
        :param data:
        :return: None.
        """
    try:
        bus.write_byte_data(addr, reg, data)
        print(f"Written {data} to register {reg}")
    except Exception as e:
        print(f"I2C write error: {e}")
