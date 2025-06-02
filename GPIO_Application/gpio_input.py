#-------------------------------------------------------------------------------------------------------------------
# GPIO Input Control Application using gpiod library
#-------------------------------------------------------------------------------------------------------------------
import gpiod
from gpiod.line import Direction

# GPIO Configuration Constants
#-------------------------------
GPIO_CHIP_NAME = "/dev/gpiochip0"  
GPIO_LINE = 363                    

def gpio_init(GPIO_chip_name, GPIO_line):
    """
        Function to Initialize the GPIO.
        
        :param GPIO_chip_name: It specifies the GPIO chip name (e.g., "gpiochip0").
        :param GPIO_line: It specifies the GPIO Line.
        :return: It returns the integer value of GPIO Line Number.
        """
    
    config = gpiod.LineSettings(direction=Direction.INPUT)

    request = gpiod.request_lines(
        GPIO_chip_name,
        consumer="gpio-app",
        config={GPIO_line: config}
    )
    return request

def gpio_get(request):
    """
        Function to Get the GPIO Line.
        
        :param request: It specifies the Direction of GPIO Line.
        :param GPIO_line: It specifies the input GPIO Line.
        :return: None.
        """
    return request.get_value(0)

# Main Execution
#--------------------------------------------------------------
if __name__ == "__main__":

    request = gpio_init(GPIO_CHIP_NAME, GPIO_LINE)

    current_val = gpio_get(request)
    print("GPIO value is:", "HIGH" if current_val else "LOW")

