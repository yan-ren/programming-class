# write a function, takes two inputs, chr, string, return a number represents how many chars in the string
# 'a', 'abca'
# 2

def count_letters(letter, string):
    count = 0
    for i in string:
        if i == letter:
            count += 1

    return count

def q7(string):
    result = []
    for i in string:
        count = count_letters(i, string)
        if count == 1:
            result.append(1)
        elif count > 1:
            result.append(0)
    return result