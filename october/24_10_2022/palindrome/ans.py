def palindrome(n):
    rev_n = 0
    c = n

    while n > 0:
        reminder = n % 10
        n = n // 10
        rev_n = (10*rev_n) + reminder

    if c == rev_n:
        print(c, " is a palindrome")
    else:
        print(c, " is a not a palindrome as its value is", rev_n, "after reversing")

print(palindrome(23439))