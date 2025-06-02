# GPIO Input and Output Control Application using gpiod Library.

-----------------------------------------------------------------------------------------------------------------------------------------
           
## Description

1. This Python script GPIO_input.py allows you to control a GPIO output pin using the gpiod library. It initializes a specific GPIO line and then sets its value to HIGH (1) or LOW (0). This is useful for tasks such as:

- Turning an LED ON or OFF

- Controlling relays or other digital devices

## Key Features:
Uses the gpiod library to interact with GPIO lines.

Lets you configure and set the output state (high/low) of a chosen GPIO pin.

Simple and effective for hardware control like LED blinking or toggling.

2. This Python script reads the state of a GPIO input pin using the gpiod library. It is ideal for checking whether a button is pressed, a sensor is triggered, or any digital input is active (logic HIGH or LOW).

## Key Features:
Uses the gpiod library to access GPIO input lines.

Allows you to read the current value (0 or 1) of a specified GPIO pin.

Useful for applications like reading buttons, switches, or sensors.
--------------------------------------------------------------------------------------------------------------------------------------------

## Dependencies

- python
- gpiod Python bindings (Required, version ≥ 1.6)

--------------------------------------------------------------------------------------------------------------------------------------------

## Usage

1. Make sure the gpiod tools and Python bindings are installed.
2. Run `sudo gpiodetect` to find the GPIO chip (e.g., `/dev/gpiochip0`).
3. Run `sudo gpioinfo gpiochip0` to find the correct GPIO line number.
4. Update the `GPIO_LINE` value in the script accordingly.
5. Run the script using sudo:
   ```bash
   sudo python3 gpio_control.py
--------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------
## GPIO Configuration Constants
--------------------------------------------------------------------------------------------------------------------------------------------
GPIO_CHIP_NAME = "/dev/gpiochip0"
    - The GPIO chip device path.

GPIO_LINE = 363
    - The line number to control input and output (change this according to your hardware).

--------------------------------------------------------------------------------------------------------------------------------------------
## Function: gpio_init(GPIO_chip_name, GPIO_line)
--------------------------------------------------------------------------------------------------------------------------------------------
Description:
    Initializes the GPIO line for Input and output.

Parameters:
    GPIO_chip_name (str): Path to the GPIO chip (e.g., /dev/gpiochip0)
    GPIO_line (int): Line number to configure inside code

Returns:
    gpiod.LineRequest: An object to control the GPIO line

--------------------------------------------------------------------------------------------------------------------------------------------
## Function: gpio_set(request, GPIO_line, state)
--------------------------------------------------------------------------------------------------------------------------------------------
Description:
    Sets the GPIO line value to either HIGH (1) or LOW (0)

Parameters:
    request (gpiod.LineRequest): The request object returned from gpio_init
    GPIO_line (int): Line number to set
    state (int): 1 to set HIGH, 0 to set LOW

--------------------------------------------------------------------------------------------------------------------------------------------
## Main Execution Logic
--------------------------------------------------------------------------------------------------------------------------------------------
1. Prompt the user to input the GPIO state (0 or 1)
2. Initialize the GPIO using gpio_init()
3. Start a loop to blink the GPIO ON and OFF every second using gpio_set()
4. Press Ctrl+C to stop the loop

--------------------------------------------------------------------------------------------------------------------------------------------
## Example Output:
--------------------------------------------------------------------------------------------------------------------------------------------
Blinking GPIO line 363 on /dev/gpiochip0 (Press Ctrl+C to stop)
(on, off ...)

--------------------------------------------------------------------------------------------------------------------------------------------
## Notes:
--------------------------------------------------------------------------------------------------------------------------------------------
- This script requires to access GPIO lines.
- Adapt GPIO_LINE based on your hardware and available GPIO pins.
