
# UART Control Application Documentation

This application enables simple UART (Universal Asynchronous Receiver/Transmitter) communication using Python’s `pyserial` library. It allows the user to send and receive serial data through a specified COM port.

---

## 📁 File Structure

```
UART-Application/
├── main.py           # Main script for UART communication
├── uart_send.py      # Contains function to send data over UART
├── uart_receive.py   # Contains function to receive data over UART
           
```

---

## Requirements

- Python 
- `pyserial` library  
  Install it using:
  ```bash
  pip install pyserial
  ```

---

## How It Works

### **Step 1: Run `main.py`**
This is the main driver script. It:
- Lists available UART/COM ports.
- Prompts the user to select a port.
- Initializes UART.
- Sends user input to the selected UART device.
- Receives and displays any data returned by the device.

### Example:
```bash
python main.py
```

---

## Function Overview

### `main.py`

#### `list_uart_ports()`
Lists all available serial ports on your system.

#### `uart_init(port, baud_rate)`
Initializes a UART connection.
- **port**: COM port (e.g., `"COM3"` or `"/dev/ttyUSB0"`)
- **baud_rate**: Typically 9600, 115200, etc.
- **Returns**: Serial object if successful, otherwise `None`.

---

### `uart_send.py`

#### `uart_send(serial_obj, data)`
Sends string data through UART.
- **serial_obj**: The initialized UART object.
- **data**: The string to send.
- Encodes and transmits the string via UART.

---

### `uart_receive.py`

#### `uart_receive(serial_obj)`
Receives all available data from UART.
- **serial_obj**: The UART object.
- Reads and decodes incoming data.
- Prints received data or shows a message if nothing is received.

---

## Sample Interaction

```bash
Available UART Ports:
COM3 - USB Serial Device
Enter the com port: COM3
Opened UART on COM3 at 115200 baud rate
Enter data to send over UART: Hello World
Sent: Hello World
Received: OK
```

---

## ⚠️ Notes

- Ensure the target UART device is connected before running the script.
- Baud rate and port must match your connected device’s configuration.
- Use a proper USB-to-Serial adapter for physical UART connections if required.

---

