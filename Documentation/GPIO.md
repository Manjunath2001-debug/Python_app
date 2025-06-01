# GPIO Input and Output Control Application using gpiod Library

----------------------------------------------------------------------------------------------------------------

## Description

This Python script controls a GPIO line using the Linux **gpiod** library. It initializes a specific GPIO line  
and set and get the same line. It is useful for blinking an LED or toggling a digital output.

-----------------------------------------------------------------------------------------------------------------

## Dependencies

- gpiod Python bindings (Required, version ≥ 1.6)
------------------------------------------------------------------------------------------------------------------

## Usage

1. Make sure the gpiod tools and Python bindings are installed.
2. Run `sudo gpiodetect` to find the GPIO chip (e.g., `/dev/gpiochip0`).
3. Run `sudo gpioinfo gpiochip0` to find the correct GPIO line number.
4. Update the `GPIO_LINE` value in the script accordingly.
5. Run the script using sudo:
   ```bash
   sudo python3 gpio_control.py
------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------
## GPIO Configuration Constants
----------------------------------------------------------------------------------------------------------------
GPIO_CHIP_NAME = "/dev/gpiochip0"
    - The GPIO chip device path.

GPIO_LINE = 363
    - The line number to control input and output (change this according to your hardware).

-----------------------------------------------------------------------------------------------------------------
## Function: gpio_init(GPIO_chip_name, GPIO_line)
-----------------------------------------------------------------------------------------------------------------
Description:
    Initializes the GPIO line for Input and output.

Parameters:
    GPIO_chip_name (str): Path to the GPIO chip (e.g., /dev/gpiochip0)
    GPIO_line (int): Line number to configure inside code

Returns:
    gpiod.LineRequest: An object to control the GPIO line

-------------------------------------------------------------------------------------------------------------
## Function: gpio_set(request, GPIO_line, state)
-------------------------------------------------------------------------------------------------------------
Description:
    Sets the GPIO line value to either HIGH (1) or LOW (0)

Parameters:
    request (gpiod.LineRequest): The request object returned from gpio_init
    GPIO_line (int): Line number to set
    state (int): 1 to set HIGH, 0 to set LOW

-------------------------------------------------------------------------------------------------------------
## Main Execution Logic
-------------------------------------------------------------------------------------------------------------
1. Prompt the user to input the GPIO state (0 or 1)
2. Initialize the GPIO using gpio_init()
3. Start a loop to blink the GPIO ON and OFF every second using gpio_set()
4. Press Ctrl+C to stop the loop

-----------------------------------------------------------------------------------------------------------
## Example Output:
------------------------------------------------------------------------------------------------------------
Blinking GPIO line 363 on /dev/gpiochip0 (Press Ctrl+C to stop)
(on, off ...)

-------------------------------------------------------------------------------------------------------------
## Notes:
-------------------------------------------------------------------------------------------------------------
- This script requires to access GPIO lines.
- Adapt GPIO_LINE based on your hardware and available GPIO pins.
