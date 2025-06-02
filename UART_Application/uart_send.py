#>> Function to send the data through UART Peripheral.
#----------------------------------------------------------------------------

def uart_send(serial_obj, data):
    """
        Function to receive the uart data.
        
        :param serial_obj: It specifies the object received from the uart.
        :param data: It specifies the data to sent through uart.
        :return: None.
        """
    if serial_obj:

        serial_obj.write(data.encode('utf-8'))
        print(f"Sent: {data}")

