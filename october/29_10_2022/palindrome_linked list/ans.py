def palindrome_list(lst):

    new_list = [lst[len(lst) - i]
            for i in range(1, len(lst)+1)]
    if new_list == lst:
        return True
    else:
        return False
original_list = [1,2,3,2,1]
print(palindrome_list(original_list))