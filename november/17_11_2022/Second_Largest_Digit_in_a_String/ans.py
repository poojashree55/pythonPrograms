def secondHighest(s):
    l = []
    for i in s:
        if i.isdigit() and i not in l:
            l.append(i)
    if len(l) >= 2:
        return int(sorted(l)[-2])
    else:
        return -1

s = "dfa12321afd"
print(secondHighest(s))