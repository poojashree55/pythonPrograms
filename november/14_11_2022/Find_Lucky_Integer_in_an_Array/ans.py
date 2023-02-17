def findLucky(arr):
    large = -1
    unique = set(arr)
    for item in unique:
        count = arr.count(item)
        if item == count:
            large = max(large, item)
    return large

arr = [1,2,2,3,3,3]
print(findLucky(arr))
