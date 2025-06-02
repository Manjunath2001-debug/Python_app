import time 

def uart_receive(serial_obj):
    """
        Function to receive the uart data.
        
        :param serial_obj: It specifies the object received from the uart.
        :return: It returns the received data from the uart.
        """
    
    if serial_obj:
        time.sleep(0.1)
        data = serial_obj.read_all().decode('utf-8').strip()
        if data:
            print(f"Received: {data}")
        else:
            print("NO Received data!")
        return data
    return None


