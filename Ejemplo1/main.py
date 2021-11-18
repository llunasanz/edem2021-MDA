import datetime as dt
import time

while True:
    # Print current time and sleep 1 minute
    print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(60)
