import csv
import time
import datetime
import pytz

from .models import ReviewModel


def time_to_datetime(time_data: int):
    t = time.gmtime(time_data)
    time_tuple = (t.tm_year, t.tm_mon, t.tm_hour)

    return datetime.datetime(*time_tuple, 0, 0, tzinfo=pytz.UTC)


def save_data(*args):
    user_id = int(args[0])
    trip_id = int(args[1])
    rating = float(args[2])
    timestamp = time_to_datetime(int(args[3]))

    ReviewModel(user_id=user_id, trip_id=trip_id, rating=rating, timestamp=timestamp).save()


def import_data(file_name):
    f = open(file_name, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        save_data(*line)
    f.close()




