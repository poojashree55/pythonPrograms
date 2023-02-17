def replaceElements(arr):
    m = -1
    i = len(arr) -1
    while i >= 0:
        temp = arr[i]
        arr[i] = m
        if temp > m:
            m = temp
        i-= 1
    return arr

arr = [17,18,5,4,3,6]
print(replaceElements(arr))
