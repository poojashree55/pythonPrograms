def findDifference(nums1,nums2):
    s1 = set(nums1)
    s2 = set(nums2)

    nums1 = list(s1)
    nums2 = list(s2)

    s = []
    for i in range(len(nums1)):
        if nums1[i] not in s2:
            s.append(nums1[i])
    d = []
    for i in range(len(nums2)):
        if nums2[i] not in s1:
            d.append(nums2[i])

    res = []
    res.append(s)
    res.append(d)
    return res

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1,nums2))
