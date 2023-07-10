def height_checker(input):
    expected = sorted(input)
    result = 0
    for x, y in zip(input, expected):
        if x != y:
            result += 1

    return result


l = [1, 2, 3, 4]
l.sort()

sorted(l)

'''
zip more example
'''
a = ('a', 'b', 'c')
b = ('e', 'f', 'g')
c = ('h', 'i', 'j')

print(list(zip(a, b, c)))

a = ('a', 'b', 'c')
b = ('e', 'f')

print(list(zip(a, b)))