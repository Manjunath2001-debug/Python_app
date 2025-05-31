#-------------------------------------------------------------------------------------------------------------
# GPIO Input Control Application using gpiod library
#-------------------------------------------------------------------------------------------------------------
import gpiod
from gpiod.line import Direction, Value

#-------------------------------------------------------------------------------------------------------------
# GPIO Configuration Constants
#-------------------------------------------------------------------------------------------------------------
GPIO_CHIP_NAME = "/dev/gpiochip0"  # Use 'sudo gpiodetect' to find the chip name
GPIO_LINE = 363                    # Use 'gpioinfo gpiochip0' to find the correct GPIO line
#-------------------------------------------------------------------------------------------------------------
# Function: gpio_init()
# Description: Initializes the GPIO line for Input
#-------------------------------------------------------------------------------------------------------------
def gpio_init(GPIO_chip_name, GPIO_line):
    
    config = gpiod.LineSettings(direction=Direction.INPUT)

    request = gpiod.request_lines(
        GPIO_chip_name,
        consumer="gpio-app",
        config={GPIO_line: config}
    )
    return request
#-------------------------------------------------------------------------------------------------------------
# Function: gpio_get()
# Description: gets the GPIO line value (HIGH/LOW)
#-------------------------------------------------------------------------------------------------------------
def gpio_get(request, GPIO_line):
    return request.get_value(GPIO_line)
#-------------------------------------------------------------------------------------------------------------
# Main Execution
#-------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    request = gpio_init(GPIO_CHIP_NAME, GPIO_LINE)

    current_val = gpio_get(request, GPIO_LINE)
    print("GPIO value is:", "HIGH" if current_val else "LOW")

