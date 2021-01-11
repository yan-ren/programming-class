# a = [1, 2, 3]
# b = 1, 2, 3
#
# a[0] = 100
# print(b[0])
# b = (1, 2) # reassignment
# # immutable: once create the object and assign some value to it, cannot modify/change that value
#
# # practice: write a function takes a tuple as input, return the list with same values
# # (1, 2, 3) -> [1, 2, 3]
# # practice: write a function takes a tuple as input, return the list with same values but reversed order
# # (1, 2, 3) -> [3, 2, 1]
#
# test = (1, 2, 3)
# test_list = list(test)
# print(test_list)
#
# test1 = [1, 2, 3]
# print(test1[::-1])
# test1_tuple = tuple(test1)[::-1]
# print(test1_tuple)

def return_multiple():
    a = 1
    b = 2
    c = 3
    return a, b, c


result1, result2 = return_multiple()
print(type(result1))
print(result1)

