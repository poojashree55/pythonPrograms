l = [2,3,7,8,5,1]
target = 9

for i in range(len(l)-1):
    for j in range(1,len(l)):
        if l[i] + l[j] == target:
            print(i, j)