import datetime
import time

halloween2016 = datetime.datetime(2019, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
