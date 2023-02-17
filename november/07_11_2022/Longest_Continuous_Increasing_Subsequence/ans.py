def findLengthOfLCIS(nums):
    msf = 0  # maxim so far
    meh = 1  # maxim ending here
    n = len(nums)
    if n == 1:
        return 1
    last = nums[0]
    for i in range(1, n):
        if nums[i] > last:
            last = nums[i]
            meh += 1
        else:
            meh = 1
            last = nums[i]
        if msf < meh:
            msf = meh
    return msf

nums = [1,3,5,6,9]
print(findLengthOfLCIS(nums))
