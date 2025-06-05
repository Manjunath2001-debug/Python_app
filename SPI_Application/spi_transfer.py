def spi_transfer(spi, data):
    """
        Function to Transfer the SPI bus.
        
        :param spi: specifies the spi bus.
        :param data: specifies the input data. 
        :return: returns response or None.
        """

    try:
        response = spi.xfer2(data)
        print(f"Sent: {data} | Received: {response}")
        return response
    except Exception as e:
        print(f"SPI transfer error: {e}")
        return None