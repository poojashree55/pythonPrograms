def numDifferentIntegers(word):
    nums = "0123456789"
    for i in range(len(word)):
        if word[i] not in nums:
            word = word.replace(word[i], " ")
            print('word', word)

    w = word.split()
    print('w',w)
    for i in range(len(w)):
        w[i] = int(w[i])
        print('w[i]', w[i])
    w = set(w)
    return len(w)

word = "leet1234code234"
print(numDifferentIntegers(word))
