import time
import datetime


def time_to_datetime(time_data: int):
    t = time.gmtime(time_data)
    time_tuple = (t.tm_year, t.tm_mon, t.tm_hour)

    return datetime.datetime(*time_tuple, 0, 0)