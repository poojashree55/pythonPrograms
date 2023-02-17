def stringMatching(words):

    output = []

    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] in words[j] and i != j:
                if words[i] not in output:
                    output.append(words[i])

    return output

words = ["leetcode","et","code"]
print(stringMatching(words))