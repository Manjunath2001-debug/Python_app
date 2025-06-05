# SPI Control Application using spidev Library

This application allows you to send and receive data over the SPI bus using Python and the `spidev` library. It supports user input of bytes and displays the sent and received data.

---

## Requirements

- Linux-based system 
- Python 3
- `spidev` library
  ```bash
  pip install spidev
  ```

---

## Project Structure

```
SPI_Control_Application/
│
├── spi_app.py              # Main script to initialize SPI and handle user input
├── spi_transfer.py         # Contains spi_transfer() function

```

---

## Usage

1. **Connect your SPI device** (e.g., to `/dev/spidev0.0`).
2. **Run the script**:
   ```bash
   python3 spi_app.py
   ```
3. **Enter comma-separated bytes** when prompted:
   ```
   Enter comma-separated bytes (e.g., 0x01,0x02): 0xA5, 0x5A
   ```

4. **Output Example**:
   ```
   Sent: [165, 90] | Received: [255, 127]
   ```

---

## Code Explanation

### `spi_init(bus, device)`

Initializes and returns the SPI object.
- Opens the SPI bus and device (e.g., `/dev/spidev0.0`)
- Sets `max_speed_hz` (e.g., 50kHz)

### `spi_transfer(spi, data)`

Transfers the given list of bytes over SPI.
- Uses `spi.xfer2()` to send and receive data
- Prints sent and received byte lists

### `main` loop

- Reads user input as comma-separated byte values (hex or decimal)
- Converts them to a list of integers
- Calls `spi_transfer()`

---

## Exit

To stop the script, press `Ctrl + C`. The SPI bus is closed cleanly.


## Troubleshooting

- Ensure SPI is enabled via `config`
- Check correct SPI device path (usually `/dev/spidev0.0`)
- Make sure your SPI slave device is powered and wired correctly

---
