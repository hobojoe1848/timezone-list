import pendulum
import pytz


def create_list():
    tz_list = []
    for tz in pytz.all_timezones:
        tz_list.append(tz)
    return tz_list


def get_tz_time(choice):
    try:
        return pendulum.now(choice).to_datetime_string()
    except ValueError:
        raise
