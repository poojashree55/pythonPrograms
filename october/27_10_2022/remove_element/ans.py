def removeDuplicates(nums):
    c = 1
    for i in range(1,len(nums)):
        if nums[i-1]!=nums[i]:
            nums[c] = nums[i]
            c+=1
    return c
lst = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(lst))
