def majorityElement(nums):
    nums.sort()
    print(nums)
    N = len(nums)
    print("len: ", N)
    count = 1
    if N > 1:

        for i in range(1, N):
            if nums[i - 1] == nums[i]:
                count += 1
            else:
                count = 1

            if count > N // 2:
                return nums[i]

    else:
        return nums[0]

lst = [2,2,1,1,1,2,2]
print(majorityElement(lst))