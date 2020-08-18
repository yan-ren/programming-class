# write a function that counts the numbers for each value
# list = [1, 2, 3, 3, 1]
# [2, 1, 2, 2, 2]

# def count(list):
#     res = []
#     for i in list:
#         res.append(list.count(i))
#     return res


# def count(list, target):
#     counter = 0
#     for i in list:
#         if i == target:
#             counter += 1
#
#     return counter

# write a function that takes a list return the element of highest frequency
# list = [1, 2, 2, 2, 3, 3, 3]
def find_most(list):
    frequency = 0
    value = list[0]
    for i in list:
        count = list.count(i)
        if count > frequency:
            frequency = count
            value = i

    return value

# example: list = [1, 2, 3]
# return [1, 1, 2, 2, 3, 3]
# input [1, 2, 2, 3]
# return [1, 1, 2, 2, 2, 2, 3, 3]
def create_list(list):
    index = 0
    while index < 2 * len(list):
        list.insert(index + 1, list[index])
        index += 2
    return list


list = [100, 21, 30, 14]
del list[0:3]
print(list)
# print(list)
# list.sort(reverse=True)
# print(list)

# write a function that takes a list, find out the most frequent value, and remove it
# example: list = [1, 2, 3, 3, 3]
# return: [1, 2]