# USB Mass Storage Read/Write Test Script

This Python script performs the following:

- Detects connected USB devices using `pyusb`.
- Identifies USB Mass Storage Class devices.
- Performs a read/write test to ensure proper functionality.
- Cleans up the test file afterward.

---

## Requirements

Ensure the following packages are installed:

```bash
pip install pyusb psutil
```

---

## 📁 Folder Structure

```
project/
│
├── usb_storage.py        # Contains test_mass_storage function
├── main.py               # Main execution script
```

---

## 📝 Notes

- Make sure `/mnt/usb` exists and the USB is mounted there.
- If `/dev/sda1` is the USB, you can mount it using:

```bash
sudo mkdir -p /mnt/usb
sudo mount /dev/sda1 /mnt/usb
```
