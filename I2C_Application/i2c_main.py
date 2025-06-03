#-------------------------------------------------------------------------------------------------------------
# I2C Control Application using smbus2 library.
#-------------------------------------------------------------------------------------------------------------
import time
from smbus2 import SMBus
from i2c_read import i2c_read  

def i2c_init(bus_num):
    """
        Function to Initialize the I2C.
        
        :param bus_num: It specifies the I2C bus.
        :return: It returns the bus or None.
        """
    try:
        bus = SMBus(bus_num)
        print(f"I2C bus {bus_num} initialized.")
        return bus
    except Exception as e:
        print(f"Failed to initialize I2C: {e}")
        return None

#-------------------------------------------------------------------------------------------------------------
# Main Execution
#-------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    i2c_bus = int(input("Enter the I2C bus: "))
    i2c_addrs = int(input("Enter the I2C address: "))
    register = int(input("Enter the device register: "))

    bus = i2c_init(i2c_bus)
    
    if bus:
        try:
            while True:
                ret = i2c_read(bus, i2c_addrs, register)
                print(f"Data read from the device :{ret}")
                time.sleep(1) # read data every second
        
        except KeyboardInterrupt:
            print("\nI2C communication stopped.")
        finally:
            bus.close()
