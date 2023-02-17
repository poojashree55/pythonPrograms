def findErrorNums(nums):
    n = len(nums)
    s = n*(n+1)//2
    print('s',s)
    miss = s - sum(set(nums))
    duplicate = sum(nums) + miss - s
    return [duplicate, miss]
nums = [1,2,2,4]
print(findErrorNums(nums))