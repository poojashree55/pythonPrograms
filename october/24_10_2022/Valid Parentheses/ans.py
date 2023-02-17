def check(braces):
    open_tup = tuple('({[')
    closing_tup = tuple(')}]')
    map = dict(zip(open_tup, closing_tup))
    list_1 = []

    for i in braces:
        if i in open_tup:
            list_1.append(map[i])
        elif i in closing_tup:
            if not list_1 or i != list_1.pop():
                return "Unbalanced"
    if not list_1:
        return "Balanced"
    else:
        return "Unbalanced"

string = "{[]{()}}"
print(string, "-", check(string))

string = "{([)]}"
print(string, "-", check(string))