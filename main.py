import psutil
from plyer import notification
import time


def conversion(sec):    # Will convert seconds into Hrs and minutes
    second = sec % (24*3600)
    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    return hour, minute


while True:
    battery = psutil.sensors_battery()  # Gets battery information
    h, m = conversion(battery.secsleft)     # Converting them into hours and minutes
    notification.notify(    # Notifying
        title="Battery Percentage",
        message=f'{h}Hr {m}Min {battery.percent}% remaining',
        timeout=10
    )
    time.sleep(60*60)   # Notifies every hour
