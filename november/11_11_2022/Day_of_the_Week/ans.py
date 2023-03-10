def dayOfTheWeek(day, month, year):
    prev_year = year - 1
    days = prev_year * 365 + prev_year // 4 - prev_year // 100 + prev_year // 400
    #print('days',days)
    days += sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1])
    days += day

    if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        days += 1

    return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][days % 7]


day = 18
month = 7
year = 1999

print(dayOfTheWeek(day, month, year))