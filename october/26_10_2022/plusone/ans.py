def plus_one(list_one):
    if list_one[-1]<9:
        list_one[-1] = list_one[-1]+1
        print("after adding:",list_one)
    else:
        s = ""
        for i in list_one:
            s +=str(i)
            print(s)
        s = int(s)+1
        s = str(s)
        print("s value: ",s)
        list_two=[]
        for char in s:
            list_two.append(char)
        return list_two

l = [8, 6, 7, 9]
print(plus_one(l))