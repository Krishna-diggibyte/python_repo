import calendar
import logging

logging.basicConfig(level=logging.INFO ,format='%(message)s')


def find_day():
    date = input()
    d_month, d_date, d_year = (int(i) for i in date.split(' '))
    day_no = calendar.weekday(d_year, d_month, d_date)
    # print(day_no)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    logging.info(days[day_no].upper())
    return days[day_no].upper()



