#-------------------------------------------------------------------------------------------------------------
# SPI Control Application using spidev
#-------------------------------------------------------------------------------------------------------------
import spidev
from spi_transfer import spi_transfer
import time 
#------------------------------------------------------------------------------------------------------------
SPI_BUS = 0
SPI_DEVICE = 0
#-------------------------------------------------------------------------------------------------------------
def spi_init(bus, device):
    """
        Function to Initializes the SPI bus.
        
        :param bus: specifies the spi bus.
        :param device: specifies the spi device. 
        :return: returns spi or None.
        """
    try:
        spi = spidev.SpiDev()
        spi.open(bus, device)
        spi.max_speed_hz = 50000
        print(f"SPI bus {bus}, device {device} initialized.")
        return spi
    except Exception as e:
        print(f"Failed to initialize SPI: {e}")
        return None

#-------------------------------------------------------------------------------------------------------------
# Main Execution
#-------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    spi = spi_init(SPI_BUS, SPI_DEVICE)
    if spi:
        try:
            while True:
                user_input = input("Enter comma-separated bytes or 'exit' to quit: ")
                if user_input.lower() in ('exit', 'quit'):
                    break
                try:
                    byte_list = [int(b.strip(), 0) for b in user_input.split(',')]
                except ValueError:
                    print("Invalid input. Please enter bytes like 0x01,0x02.")
                    continue
                spi_transfer(spi, byte_list)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nSPI communication stopped.")
        finally:
            spi.close()
