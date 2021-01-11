# homework: write a method that takes a tuple as input, return the tuple with the largest value removed
# input (1, 2, 3)
# output (1, 2)
# input (1, 2, 3, 3, 3)
# output (1, 2)

# one solution: convert to the question we seen before - remove the largest value from the list
def remove_largest_from_tuple(t):
    l = list(t)

    # remove the largest value from the list l
    new_l = []
    max_value = max(l)

    for i in l:
        if i != max_value:
            new_l.append(i)

    return tuple(new_l)


def values():
    a = 1
    b = 2
    return a, b


result1, result2 = values()
print(result1)
print(type(result1))


def quick_math(a, b, c):
    return a + b - c


boom = (2, 2, 1)
quick_math(*boom)


dic = {1:"first", 2:"second"}
print(dic[1])
print(dic[2])
dic[20] = "twentieth"
print(dic)