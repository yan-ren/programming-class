# tuple = 1, 2, 3 # pack three values into a tuple
# print(tuple)
# print(type(tuple))
# # unpacking means put each value in tuple into independent variable
# a, b, c = tuple
# print(a)
# print(b)
# print(c)
#
# # swap the value between a and b
# a = 1
# b = 2
#
# print(a, b)
# # c = a
# # a = b
# # b = c
# #      (2, 1)
# a, b = b, a
# print(a, b)

# write a function,
# get the first n values in the fib sequence

# def fib(n):
#     a = 0
#     b = 1
#
#     print(a)
#     print(b)
#
#     for i in range(n - 2):
#         print(a + b)
#         a, b = b, a + b
#
# fib(12)

# def quick_math(a, b, c):
#     return a + b - c
#
# boom = (2, 2, 1)
# print(quick_math(*boom))

# a = {'a': 1, 'b': 1}
# a['a'] = a['a'] + 1
# a['c'] = 1
# print(a)

# write a function given a string as a input, returns a dictionary where the key is the charater in string,
# the value is the frequency of the character
# a = "aaabbc"
# {"a": 3, "b": 2, "c": 1}

# d = {"one": 1}
# d["12"] = d["one"] + 1
# print(d)

# Expected Result : {0: 10, 1: 20, 2: 30, 3:40,  .... 9:100}

i = 0
test = {}
while i <= 9:
    test[i] = (i + 1) * 10
    i += 1

# get a list of keys
print(test.keys())

# get a list of values
print(test.values())
# for i in test.values():
#     print(i)

# get a list of items
print(test.items())
for i in test.items():
    print(i[0], i[1])


# use the dictionary:test, writes a functions
# get the sum of all keys and all values
def sum_of_dic(dic):
    key_sum = 0
    value_sum = 0
    # for key in dic.keys():
    #     key_sum += key
    #
    # for value in dic.values():
    #     value_sum += value
    # for item in dic.items():
    #     key_sum += item[0]
    #     value_sum += item[1]
    for i, j in dic.items():
        pass
    return key_sum, value_sum


for i, j in test.items():
    print(i, j)


for item in test.items():
    print(item[0])
    print(item[1])


# item=pair in dictionary,
# one item(pair) has one key and one value

a = (1, 2)
x, y = a
print(x)
print(y)