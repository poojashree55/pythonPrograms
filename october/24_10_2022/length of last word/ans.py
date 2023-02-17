def len_Last_Word(s):
    leng = 0
    x = s.strip()

    for i in range(len(x)):
        if x[i] == " ":
            leng = 0
        else:
            leng += 1
    return leng

if __name__ == "__main__":
    y = "I am practicing leetcode programs"
    print("The length of last word is: ",
          len_Last_Word(y))

