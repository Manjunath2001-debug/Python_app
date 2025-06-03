
# I2C Control Application using smbus2

This Python application demonstrates basic I2C communication using the `smbus2` library. It allows reading from and writing to I2C device registers.

---

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Error Handling](#error-handling)

---

## Overview

This application initializes the I2C bus, reads data from a specified register of an I2C device, and supports writing data to the device register. It uses the `smbus2` Python library for I2C communication.

---

## Requirements

- Python 3.x
- `smbus2` library

---

## Installation

Install the required Python library via pip:

```bash
pip install smbus2
```

---

## Usage

1. Connect your I2C device to the I2C bus (default bus 1).
2. Modify the I2C device address and register in the script if needed.
3. Run the script:

```bash
python your_script.py
```

---

## Functions

### `i2c_init(bus_num)`

Initializes the I2C bus.

- **Parameters:**
  - `bus_num` (int): The I2C bus number (usually 1 on Raspberry Pi).
- **Returns:** 
  - SMBus object if successful, otherwise `None`.

---

### `i2c_read(bus, addr, reg)`

Reads a byte of data from a specific register on the I2C device.

- **Parameters:**
  - `bus`: SMBus object.
  - `addr` (int): I2C device address.
  - `reg` (int): Register address to read from.
- **Returns:** 
  - Integer value read from the register, or `None` if an error occurs.

---

### `i2c_write(bus, addr, reg, data)`

Writes a byte of data to a specific register on the I2C device.

- **Parameters:**
  - `bus`: SMBus object.
  - `addr` (int): I2C device address.
  - `reg` (int): Register address to write to.
  - `data` (int): Data byte to write.
- **Returns:** 
  - None.

---

## Error Handling

- The application handles exceptions during I2C bus initialization, read, and write operations.
- On failure, appropriate error messages are printed, and operations safely exit.


