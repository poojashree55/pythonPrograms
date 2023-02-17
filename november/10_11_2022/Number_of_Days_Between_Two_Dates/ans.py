def daysBetweenDates(date1, date2):
    if date1>date2:
        date1, date2 = date2, date1
    months = [31,28,31,30,31,30,31,31,30,31,30,31]

    d1, d2 = int(date1[8:]), int(date2[8:])
    m1, m2 = int(date1[5:7]), int(date2[5:7])
    y1, y2 = int(date1[:4]), int(date2[:4])

    def num_days(d, m, y):
        return (y-1)*365+((y-1)//400+(y-1)//4-(y-1)//100)+sum(months[:m-1])+(m>2 and (y%4==0 and not y%100==0 or y%400==0))+d

    return num_days(d2, m2, y2)-num_days(d1, m1, y1)


date1 = "2020-01-15"
date2 = "2019-12-31"

print(daysBetweenDates(date1, date2))
