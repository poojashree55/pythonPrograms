def minDeletionSize(strs):
    width = len(strs[0])
    print('width',width)
    height = len(strs)
    print('height',height)
    unsorted = 0

    for col in range(width):

        for row in range(1, height):

            if strs[row-1][col] > strs[row][col]:
                print('strs[row-1][col]',strs[row-1][col])
                print('strs[row][col]',strs[row][col])
                unsorted += 1
                break
    return unsorted

strs = ["cba","daf","ghi"]
print(minDeletionSize(strs))

