def searchInsert(nums):
    target = 5
    for i,v in enumerate(nums):
        if v==target:
            return i
        elif(nums[i-1]<target<nums[i]):
            return i
        elif(target>nums[len(nums)-1]):
            return len(nums)
    return 0
lst = [2,4,3,6,7]
print(searchInsert(lst))