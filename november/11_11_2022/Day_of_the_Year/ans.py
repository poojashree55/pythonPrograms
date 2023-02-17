def dayOfYear(date):
    y, m, d = map(int, date.split('-'))
    print('y', y)
    print('m', m)
    print('d', d)
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)): days[1] = 29
    print('sum',sum(days[:m-1]))
    return d + sum(days[:m-1])

date = "2019-05-10"
print(dayOfYear(date))

