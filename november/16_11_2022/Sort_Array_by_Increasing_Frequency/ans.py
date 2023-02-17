def frequencySort(nums):
    d = {}
    count = 0
    output = []
    nums.sort()
    print('nums.sort()', nums.sort())
    print('set(nums)', set(nums))

    for i in set(nums):
        print('d',d)
        if nums.count(i) not in d:
            d[nums.count(i)] = [i]
        else:
            d[nums.count(i)].append(i)
    #         sort lists in the dictonary
    for i in d:
        d[i].sort()

    for i in sorted(d):

        if len(d[i]) == 1:
            for j in range(i):
                output.append(d[i][0])
        else:

            for j in reversed(d[i]):
                for k in range(i):
                    output.append(j)
    return output

nums = [2,3,1,3,2]
print(frequencySort(nums))