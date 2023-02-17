def singleNumber(nums):
    total  = sum(nums)
    numbers = set(nums)
    for num in numbers:
        total -= 2*num
    return -total
lst = [2,1,1,2,5,3,3]
print(singleNumber(lst))