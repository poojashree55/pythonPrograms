def reorderSpaces(text):
    word_list = text.split()
    #print('word_list',word_list)
    words, spaces = len(word_list), text.count(" ")
    # print('words', words)
    # print('spaces', spaces)

    if words > 1:
        q, r = spaces//(words-1), spaces%(words-1)
    else:
        q, r = 0, spaces

    return (" " * q).join(word_list) + " " * r

text = "  this   is  a sentence "
print(reorderSpaces(text))