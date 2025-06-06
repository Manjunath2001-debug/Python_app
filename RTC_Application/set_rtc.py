import fcntl
import struct
RTC_SET_TIME = 0x4024700a
#------------------------------------------------------------------------------------------------
def set_rtc_time(year, month, day, hour, minute, second):
    """
        Function to set the time for rtc.
        
        :param year: specifies the year to set.
        :param month: specifies the month to set.
        :param day: specifies the day to set.
        :param hour: specifies the hour to set.
        :param minute: specifies the minute to set.
        :param second: specifies the second to set.
        :return: returns spi or None.
        """
    from rtc import RTC_DEVICE # To overcome circular error need to import inside the function.
    try:
        with open(RTC_DEVICE, "wb") as rtc:
            # Linux struct rtc_time has 9 int fields:
            # tm_sec, tm_min, tm_hour, tm_mday, tm_mon, tm_year, tm_wday, tm_yday, tm_isdst
            tm = struct.pack("9i",
                second,            # tm_sec
                minute,            # tm_min
                hour,              # tm_hour
                day,               # tm_mday
                month - 1,         # tm_mon (0-11)
                year - 1900,       # tm_year (years since 1900)
                0, 0, -1           # tm_wday, tm_yday, tm_isdst (ignored)
            )
            fcntl.ioctl(rtc, RTC_SET_TIME, tm)
            print("RTC time set successfully.")
    except Exception as e:
        print(f"Error setting RTC: {e}")