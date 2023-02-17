def uniqueOccurrences(arr):
    d, ans = {}, []
    for n in arr:
        if n not in d: d[n] = 1
        else: d[n] += 1
    for n in d:
        ans.append(d[n])
    return sorted(ans) == sorted(set(ans))

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr))

