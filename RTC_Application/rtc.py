#------------------------------------------------------------------------------------------------------------------
#>> Sample application code for RTC peripheral.
#------------------------------------------------------------------------------------------------------------------
import fcntl
import struct
from set_rtc import set_rtc_time
#--------------------------------------------------------------------------------------------------------------------
# RTC device path (commonly /dev/rtc0)
RTC_DEVICE = "/dev/rtc0"
# RTC_RD_TIME 
RTC_RD_TIME = 0x80247009
#--------------------------------------------------------------------------------------------------------------------
def read_rtc_time():
    """
        Function to read the rtc time.
        :return: None.
        """
    try:
        with open(RTC_DEVICE, "rb") as rtc:
            # Read 8-byte structure: tm_sec, tm_min, tm_hour, tm_mday, tm_mon, tm_year, tm_wday, tm_yday, tm_isdst
            buf = fcntl.ioctl(rtc, RTC_RD_TIME, b"\x00" * 8 * 4)  # 8 fields, 4 bytes each
            tm = struct.unpack("8i", buf)
            year = tm[5] + 1900
            month = tm[4] + 1
            print(f"RTC Time: {year:04d}-{month:02d}-{tm[3]:02d} {tm[2]:02d}:{tm[1]:02d}:{tm[0]:02d}")
    except Exception as e:
        print(f"Error reading RTC: {e}")

if __name__ == "__main__":
    try:
        while True:
            rs = input("Read or Set (r/s): ").strip().lower()
            if rs == 'r':
                # Read once (or you can loop here, but then you need to break out)
                read_rtc_time()
            elif rs == 's':
                set_rtc_time(2025, 6, 5, 12, 45, 55)
            else:
                print("Invalid input, enter 'r', 's'.")
    except Exception as e:
        print(f"failed to read and write :{e}")
