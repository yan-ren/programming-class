# def find_min(list):
#     if len(list) == 0:
#         return None
#
#     minimum = list[0]
#
#     # for value in list:
#     #     if value < minimum:
#     #         minimum = value
#
#     index = 0
#     while index < len(list):
#         if list[index] < minimum:
#             minimum = list[index]
#
#         index += 1
#
#     return minimum
#
#
# print(find_min([1, 2, 9]))
# print(find_min([]))
#
# list = [1, 2, 3, 1, 5]
# print(len(list))
# # sum
# # method 1
# value_sum = 0
# for value in list:
#     value_sum += value
# print(value_sum)
#
# # method 2, use internal function
# print(sum(list))
#
# print(min(list))
# print(max(list))

numbers = [1, 2]
numbers.append(2)
print(numbers)
numbers.insert(0, 10)
print(numbers)

del numbers[0]
print(numbers)

numbers.remove(2)
print(numbers)
print(numbers.count(2))
print(numbers.index(2))

def count(list, target):
    counter = 0
    for value in list:
        if value == target:
            counter += 1
    return counter

