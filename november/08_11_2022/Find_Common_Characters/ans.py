def commonChars(A):
    ans = []
    for i in set(A[0]):
        print('i',i)
        x = []
        for j in A:
            x.append(j.count(i))
        a = 0
        while a < min(x):
            ans.append(i)
            a += 1
    return ans
A = ["cool","lock","cook"]
print(commonChars(A))
