# UART Control Application (Python)

This application allows you to communicate with UART (Universal Asynchronous Receiver/Transmitter) devices using Python and the `pyserial` library. It supports sending and receiving serial data and helps detect available UART ports on your system.

---

## Features

- Lists all available UART (serial) ports with descriptions.
- Initializes a selected UART port with specified baud rate.
- Allows real-time data transmission and reception via UART.
- Clean exit on keyboard interruption (`Ctrl+C`).

---

## Requirements

Install the required library

- Install pyserial 
- From  serial.tools import list_ports to list all current connected ports.
