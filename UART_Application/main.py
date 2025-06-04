#-------------------------------------------------------------------------------------------------------------
# UART Control Application using pyserial library
#-------------------------------------------------------------------------------------------------------------
import serial
import time
from serial.tools import list_ports
from uart_receive import uart_receive
from uart_send import uart_send

#-------------------------------------------------------------------------------------------------------------
# UART Configuration Constants
#-------------------------------------------------------------------------------------------------------------
BAUD_RATE = 115200          # Baud rate for UART communication
uart_port = "/dev/ttySC3"
def uart_init(port, baud_rate):
    """
        Function to initialize the uart data.
        
        :param port: It specifies the uart port.
        :param baud_rate: It specifies the uart baud rate (speed of communication bps)
        :return: None.
        """
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Opened UART on {port} at {baud_rate} baud rate")
        return ser
    except serial.SerialException as e:
        print(f"Failed to open UART: {e}")
        return None

def list_uart_ports():
    """
        Function to list the uart ports using serial.tools import list_ports.
        :return: None.
        """
    ports = list_ports.comports()
    print("Available UART Ports:")
    for port in ports:
        print(f"{port.device} - {port.description}")

#-------------------------------------------------------------------------------------------------------------
# Main Execution
#-------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    list_uart_ports()
    uart = uart_init(uart_port, BAUD_RATE)

    if uart:
        try:
            while True:
                user_input = input("Enter data to send over UART: ")
                
                uart_send(uart, user_input)

                print("Waiting for response...")
                while True:
                    if uart.in_waiting:
                        response = uart_receive(uart)
                        if response:
                            print(f"Data received successfully: Data:{response}")
                            break  # Exit the wait loop and go back to input
                        time.sleep(1)  # Poll every 100ms

        except KeyboardInterrupt:
            print("\nUART communication stopped.")
        finally:
            uart.close()
            print("UART port closed.")
