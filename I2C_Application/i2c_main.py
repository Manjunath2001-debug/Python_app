#-------------------------------------------------------------------------------------------------------------
# I2C Control Application using smbus2 library.
#-------------------------------------------------------------------------------------------------------------
import time
from smbus import SMBus
from i2c_read import i2c_read  
from i2c_write import i2c_write
from i2c_read import read_u16,read_s16
#--------------------------------------------------------------------------------------------------------------
I2C_BUS = 2
I2C_ADDRESS = 0x77
CONTROL_REG = 0xF4

TEMP_MEASURE = 0x2E # To trigger temp value
PRESSURE_MEASURE = 0x34 # To trigger pressure value
#--------------------------------------------------------------------------------------------------------------
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
    bus = i2c_init(I2C_BUS)

    if bus:
        try:
            # Read calibration constants only once
            AC5 = read_u16(bus, I2C_ADDRESS, 0xB2)
            AC6 = read_u16(bus, I2C_ADDRESS, 0xB4)
            MC  = read_s16(bus, I2C_ADDRESS, 0xBC)
            MD  = read_s16(bus, I2C_ADDRESS, 0xBE)

            while True:
                rw = input("Read or Write (r/w): ").strip().lower()
                if rw == 'w':
                    data = int(input("Enter data to write: "),0)
                    i2c_write(bus, I2C_ADDRESS, 0xF6, data)
                elif rw == 'r':
                    # Trigger temperature measurement
                    i2c_write(bus, I2C_ADDRESS, CONTROL_REG, TEMP_MEASURE)
                    time.sleep(0.005)  # 4.5 ms wait

                    # Read raw temperature from 0xF6 and 0xF7
                    msb = i2c_read(bus, I2C_ADDRESS, 0xF6)
                    lsb = i2c_read(bus, I2C_ADDRESS, 0xF7)
                    UT = (msb << 8) + lsb
                    print(f"Raw Temp: {UT}")

                    # Apply compensation formula
                    X1 = ((UT - AC6) * AC5) >> 15
                    X2 = (MC << 11) // (X1 + MD)
                    B5 = X1 + X2
                    T = (B5 + 8) >> 4
                    temp_c = T / 10.0

                    print(f"Temperature (C): {temp_c:.2f}")
                else:
                    print("Invalid choice.")
        except KeyboardInterrupt:
            print("\nI2C communication stopped.")
        except ValueError as ve:
            print(f"ValueError occurred: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            bus.close()
