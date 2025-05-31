#-------------------------------------------------------------------------------------------------------------
# GPIO Output Control Application using gpiod library
#-------------------------------------------------------------------------------------------------------------
import gpiod
import time
from gpiod.line import Direction, Value

#-------------------------------------------------------------------------------------------------------------
# GPIO Configuration Constants
#-------------------------------------------------------------------------------------------------------------
GPIO_CHIP_NAME = "/dev/gpiochip0"  # Use 'sudo gpiodetect' to find the chip name
GPIO_LINE = 363                    # Use 'gpioinfo gpiochip0' to find the correct GPIO line
#-------------------------------------------------------------------------------------------------------------
# Function: gpio_init()
# Description: Initializes the GPIO line for output
#-------------------------------------------------------------------------------------------------------------
def gpio_init(GPIO_chip_name, GPIO_line):
    
    config = gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE)

    request = gpiod.request_lines(
        GPIO_chip_name,
        consumer="gpio-app",
        config={GPIO_line: config}
    )
    return request
#-------------------------------------------------------------------------------------------------------------
# Function: gpio_set()
# Description: Sets the GPIO line value (HIGH/LOW)
#-------------------------------------------------------------------------------------------------------------
def gpio_set(request, GPIO_line, state):

    if state:
        request.set_value(GPIO_line, Value.ACTIVE)
    else:
        request.set_value(GPIO_line, Value.INACTIVE)
 
#-------------------------------------------------------------------------------------------------------------
# Main Execution
#-------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    
    request = gpio_init(GPIO_CHIP_NAME, GPIO_LINE)
       
    #Here Blink the LED Logic to check GPIO Line as HIGH and LOW 
    print(f"##### Blinking GPIO line {GPIO_LINE} (Press Ctrl+C to stop)######")
    try:
        while True:
            gpio_set(request, GPIO_LINE, True)   # Turn ON
            time.sleep(1)
            gpio_set(request, GPIO_LINE, False)  # Turn OFF
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped blinking.")

