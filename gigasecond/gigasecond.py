import datetime


def add_gigasecond(birth_date):
    gigasecond = 10**9
    return birth_date + datetime.timedelta(seconds=gigasecond)
