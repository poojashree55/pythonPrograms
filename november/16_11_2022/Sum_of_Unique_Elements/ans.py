def sumOfUnique(nums):
    ans = []
    for i in set(nums):
        if nums.count(i) == 1:
            ans.append(i)
    return sum(ans) if ans else 0

nums = [1,2,3,4,5]
print(sumOfUnique(nums))