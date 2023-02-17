def sortSentence(s):
    words = s.split()
    n = len(words)

    sent = [None] * n

    for i in range(n):
        sent[int(words[i][-1]) - 1] = words[i][:-1]

    return " ".join(sent)
s = "is2 sentence4 This1 a3"
print(sortSentence(s))
