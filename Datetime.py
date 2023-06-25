Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime as dt
import math


cost = int(input())
sale = int(input())
deliver = dt.timedelta(days=int(input()))
data = input().split('.')
data = dt.date(int(data[2]), int(data[1]), int(data[0]))
time = input().split(':')
time = dt.time(int(time[0]), int(time[1]))
if dt.time(6, 0, 0) <= time <= dt.time(12, 30, 0):
    cost -= cost / 100 * sale
    if data.weekday() != 0:
        deliver -= dt.timedelta(days=1)
a = str(data + deliver).split('-')
print('-'.join([a[2], a[1], a[0]]) + ' ' + str(math.floor(cost)))
-----------------------------------------
import datetime as dt


def alarm(date, period=10):
    date = date.split('-')
    date = dt.date(int(date[0]), int(date[1]), int(date[2]))
    start = dt.date(2021, 1, 4)
    days = (date - start).days // 7
    if days % 2 == 0:
        if date.weekday() in [0, 1, 2, 4]:
            t = dt.datetime(1, 1, 1, 8, 30)
            return (str(t.time())[:-3], str((t + dt.timedelta(minutes=period)).time())[:-3])
        elif date.weekday() in [3]:
            t = dt.datetime(1, 1, 1, 7, 45)
            return (str(t.time())[:-3], str((t + dt.timedelta(minutes=period)).time())[:-3])
        elif date.weekday() in [5, 6]:
            return "('10:00',)"
    else:
        if date.weekday() in [0, 1, 4]:
            t = dt.datetime(1, 1, 1, 9, 0)
            return (str(t.time())[:-3], str((t + dt.timedelta(minutes=period)).time())[:-3])
        elif date.weekday() in [3, 2]:
            t = dt.datetime(1, 1, 1, 9, 30)
            return (str(t.time())[:-3], str((t + dt.timedelta(minutes=period)).time())[:-3])
        elif date.weekday() in [5, 6]:
            return "('11:00',)"
------------------------------------------
from datetime import datetime, timedelta


def days_to_the_next_flight(f, v, t):
    s = list(sorted([f, v, t]))
    result = []
    dates = []
    classic = datetime.today()
    for day in s:
        if day < classic.day:
            date = datetime(classic.year, classic.month, day) + timedelta(days=30)
            if date.day != day:
                date += timedelta(days=1)
        else:
            date = datetime(classic.year, classic.month, 1) + timedelta(days=day - 1)
            if date.day != day:
                date = datetime(classic.year, classic.month + 1, 1) + timedelta(days=day - 1)
        dates.append(date)
    for date in dates:
        if date == classic or date < classic:
            continue
        elif date.weekday() == 3:
            result.append((date + timedelta(days=2) - classic).days)
        else:
            result.append((date - classic).days)
    return min(result)