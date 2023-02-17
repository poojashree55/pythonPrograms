def findNumbers(nums):
    num = map(str, nums)
    count = 0
    for s in num:
        if len(s) % 2 == 0:
            count += 1
    return count

nums = [12,345,2,6,7896]
print(findNumbers(nums))
