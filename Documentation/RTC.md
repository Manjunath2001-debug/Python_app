
# Sample application code to check the RTC Peripheral.

This script reads the current time from the onboard Real-Time Clock (RTC) on a Linux system using the `/dev/rtc0` device.

## 📋 Requirements

- Python 3
- Linux with RTC support
- RTC device available at `/dev/rtc0`
- `fcntl` and `struct` Python modules (built-in)

## How It Works

The script uses `fcntl.ioctl()` to send an `RTC_RD_TIME` request to the RTC device. It receives a C-style `struct rtc_time` containing fields such as:

- Seconds (`tm_sec`)
- Minutes (`tm_min`)
- Hours (`tm_hour`)
- Day of month (`tm_mday`)
- Month (`tm_mon`)
- Year (`tm_year`)

It then formats and prints the time.

## Output

```
RTC Time: 2025-06-05 12:00:01
RTC Time: 2025-06-05 12:00:02
RTC Time: 2025-06-05 12:00:03
...
```

## 🧪 Testing

To test the script:
1. Connect an RTC module (like DS3231 or PCF8563).
2. Ensure Linux detects it at `/dev/rtc0`.
3. Run the script:  
   ```bash
   python3 read_rtc.py
   ```

## ❗ Troubleshooting

- If you get `Error reading RTC: [Errno 2] No such file or directory: '/dev/rtc0'`, make sure the RTC is detected and enabled in your device tree or kernel config.
- Use `ls /dev/rtc*` to verify RTC presence.

