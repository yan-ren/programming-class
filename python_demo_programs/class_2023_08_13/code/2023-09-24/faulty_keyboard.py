def finalString(s):
    res = ""

    for char in s:
        if char == 'i':
            res = res[::-1]
        else:
            res += char
    
    return res