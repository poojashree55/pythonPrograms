# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# ['2', '4','5']

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
# l1.reverse()
# l2.reverse()
# print(l1,l2)

c = "".join(map(str, l1[::-1]))
d = "".join(map(str, l2[::-1]))
e = str((int(c) + int(d)))
d = list(map(int,e[::-1]))
print(d)
#'sep'.join(list)
<<<<<<< HEAD
=======
#'sep'.join(list)
>>>>>>> 30850ec07968efeeeddab893a504a31d7ed70185

