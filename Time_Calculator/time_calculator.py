def add_time(start, duration, day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_hour, start_minute_period = start.split(" ")
    start_hour, start_minute = map(int, start_hour.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))
    if start_minute_period == "PM":
        start_hour += 12
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    num_days_later = total_minutes // (24 * 60)
    total_minutes = total_minutes % (24 * 60)
    new_hour = total_minutes // 60
    new_minute = total_minutes % 60
    new_minute_str = "{:02d}".format(new_minute)
    if new_hour == 0:
        new_hour = 12
        new_period = "AM"
    elif new_hour < 12:
        new_period = "AM"
    elif new_hour == 12:
        new_period = "PM"
    else:
        new_hour -= 12
        new_period = "PM"
    new_hour_str = str(new_hour)
    if day is not None:
        day = day.capitalize()
        new_day_index = (days_of_week.index(day) + num_days_later) % 7
        new_day = days_of_week[new_day_index]
        if num_days_later == 0:
            new_time = "{0}:{1} {2}, {3}".format(new_hour_str, new_minute_str, new_period, day)
        elif num_days_later == 1:
            new_time = "{0}:{1} {2}, {3} (next day)".format(new_hour_str, new_minute_str, new_period, new_day)
        else:
            new_time = "{0}:{1} {2}, {3} ({4} days later)".format(new_hour_str, new_minute_str, new_period, new_day, num_days_later)
    else:
        if num_days_later == 0:
            new_time = "{0}:{1} {2}".format(new_hour_str, new_minute_str, new_period)
        elif num_days_later == 1:
            new_time = "{0}:{1} {2} (next day)".format(new_hour_str, new_minute_str, new_period)
        else:
            new_time = "{0}:{1} {2} ({3} days later)".format(new_hour_str, new_minute_str, new_period, num_days_later)
    return new_time


