def uart_receive(uart):
    """
        Function to receive the uart data.
        
        :param uart: It specifies the object received from the uart.
        :return: It returns the received data from the uart.
        """
    try:
        data = uart.readline().decode('utf-8', errors='ignore')
        return data.strip() if data else None
    except Exception as e:
        print(f"Receive error: {e}")
        return None
