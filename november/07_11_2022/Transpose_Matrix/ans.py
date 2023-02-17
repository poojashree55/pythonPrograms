def transpose(matrix):
    l=[]
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        l.append(temp)
    return l
matrix = [[1,4,7],[2,5,8],[3,6,9]]
print(transpose(matrix))
