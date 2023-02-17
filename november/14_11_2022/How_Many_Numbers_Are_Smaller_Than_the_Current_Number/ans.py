def smallerNumbersThanCurrent(nums):
    ans = []
    sort = sorted(nums)
    for i in nums:
        ans.append(sort.index(i))
    return ans

nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))
