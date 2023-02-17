def gcdOfStrings(str1, str2):
    while str1 != str2:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        find = str2.find(str1)
        #print('find',find)
        if find == -1:
            return ''
        str2 = str2[:find] + str2[find+len(str1):]

    return str2

str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1, str2))