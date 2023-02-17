def missingNumber(nums):
    lenth = len(nums)
    sum = (1 + lenth) * lenth/2
    for i in nums:
        sum -= i
    return sum

nums = [3,0,1]
print(missingNumber(nums))