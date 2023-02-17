def threeConsecutiveOdds(arr):
    count = 0

    for i in range(0, len(arr)):
        if arr[i] %2 != 0:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    return False

arr = [1,2,34,3,4,5,7,23,12]
print(threeConsecutiveOdds(arr))
