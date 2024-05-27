def split(numbers):
    positive = []
    negative = []

    # loop each value in numbers, if positive put in positive list, if negative, put in negative list
    for value in numbers:#
        if value >= 0:
            positive.append(value)
        else:
            negative.append(value)

    return positive, negative


print(split([1, 2, -1, -3]))

# combine function takes two lists and combine into one list
def combine(list1, list2):
    res = []
    # loop list1 and append to res

    # loop list2 and append to res

    return res


# write a function which takes a list of number and return two list
# first list contains all even number and second list contains all odd number
def even_odd(numbers):
    even = []
    odd = []

    for value in numbers:
        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)

    return even, odd
