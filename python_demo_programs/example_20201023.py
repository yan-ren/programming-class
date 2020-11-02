l = [1, 2]
t = (1, 2)

print(type(l))
print(type(t))

l[0] = 100
t[0] = 100

# homework
# write a function that takes a list as input, returns another list that contains the product of all elements except
# for the value at current index
# [1, 2, 3] -> [6, 3, 2]
# [4, 3, 2] -> [6, 8, 12]

def product(list):
    result = []
    index = 0
    while index < len(list):
        j = 0
        mul = 1
        while j < len(list):
            if j != index:
               mul = mul * list[j]
            j += 1
        result.append(mul)
        index += 1

    return result


# practice
# write a function that checks if a list contains a value that is bigger than the product of all values in the list
# [0, -1, -2, -3] -> false, because product of all values is 0, nothing in the list is bigger than 0
# [0, 1] -> true, because the product of all values is 0, 1 is in the list and bigger than 0

def solution(list):
    # product of all values
    product = 1
    for i in list:
        product = product * i

    # loop through each value check if any value is bigger than the product
    for i in list:
        if i > product:
            return True
    return False