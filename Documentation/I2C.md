
# I2C Control Application using smbus

This Python application demonstrates basic I2C communication using the `smbus` library. It allows reading from and writing to I2C device registers.

---

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Error Handling](#error-handling)
- [BMP180 Sensor Reference](#BMP180-Sensor-Reference)

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

# BMP180 Sensor Reference

The BMP180 is a popular I2C barometric pressure sensor which also measures temperature. It requires specific commands and calibration data for accurate readings.

## Key Points for Reading Temperature and Pressure

- **I2C Address:** 0x77  
- **Control Register:** 0xF4  
- **Data Registers:**  
  - 0xF6 (MSB)  
  - 0xF7 (LSB)  
  - 0xF8 (XLSB for pressure)  

---

## Reading Temperature

1. Write `0x2E` to control register (0xF4) to start temperature measurement.  
2. Wait approximately 4.5 ms for measurement to complete.  
3. Read raw temperature data from registers 0xF6 and 0xF7.  
4. Use calibration constants stored in EEPROM registers (e.g., 0xB2, 0xB4, 0xBC, 0xBE) to calculate compensated temperature.

---

## Reading Pressure

1. Write `0x34` to control register (0xF4) to start pressure measurement.  
2. Wait for measurement (depending on oversampling setting).  
3. Read raw pressure data from registers 0xF6, 0xF7, and 0xF8.  
4. Use calibration constants along with raw temperature to compute compensated pressure.

---

## Calibration Constants

These are factory-calibrated values stored in the sensor’s EEPROM. Reading these once after startup is necessary for accurate compensation.

| Register     | Description       |
| ------------ | ----------------- |
| 0xAA - 0xBB  | AC1 to AC4        |
| 0xB2         | AC5               |
| 0xB4         | AC6               |
| 0xB6 - 0xB7  | B1, B2            |
| 0xBC         | MC                |
| 0xBE         | MD                |

---

## Measurement Trigger Commands and Wait Times

| Measurement Type | Command to Write (Control Register 0xF4) | Typical Wait Time Before Reading|
|------------------|------------------------------------------|---------------------------------|
| Temperature      | 0x2E                                     | 4.5 milliseconds                |
| Pressure (OSS=0) | 0x34                                     | 4.5 milliseconds                |
| Pressure (OSS=1) | 0x74                                     | 7.5 milliseconds                |
| Pressure (OSS=2) | 0xB4                                     | 13.5 milliseconds               |
| Pressure (OSS=3) | 0xF4                                     | 25.5 milliseconds               |

*OSS = Oversampling setting; higher OSS gives more accurate pressure readings but requires longer wait.*

## Compensation Formulas

The BMP180 datasheet provides step-by-step formulas to convert raw data to actual temperature (°C) and pressure (Pa). Using the calibration constants and raw readings, you perform calculations to get real sensor values.

- Temperature compensation uses constants such as AC5, AC6, MC, MD along with the raw temperature reading.
- Pressure compensation requires additional calibration constants and takes into account the raw pressure and temperature values.

For exact formulas, refer to the BMP180 datasheet or sample implementations.

