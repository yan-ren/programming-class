def method():
    a = 1
    b = 2
    return a, b

result1, result2 = method()
# # method returns two value by putting them inside a tuple
# print(type(result1))
# print(type(result2))
#
# print(result1)
# print(result2)

# tuple packing and unpacking

value = 1, 2, 3
print(value)
print(type(value))

a, b, c = value
print(a)
print(b)

a = 1
b = 2
#      (2, 1)
a, b = (b, a)

# homework: write a method that takes a tuple as input, return the tuple with the largest value removed
# input (1, 2, 3)
# output (1, 2)
# input (1, 2, 3, 3, 3)
# output (1, 2)
