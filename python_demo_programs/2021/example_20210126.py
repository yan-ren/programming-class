# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# l = (1, 2)
# # for i in questions:
# #     print(i)
# # for i in answers:
# #     print(i)
#
# # print(zip(questions, answers))
# # zip(questions, answers) -> [('name', 'lancelot'), ('quest', 'the holy grail'), ('favorite color', 'blue')]
# for i in zip(questions, answers, l):
#     print(i)

# l1 = [1, 2, 3]
# l2 = [2, 4, 5]
# # [3, 6, 8]
# l = []
# for i, j in zip(l1, l2):
#     l.append(i + j)
# l = (3, 2, 1)
# l = sorted(l)
# print(l)
#
# a = [3, 4, 1]
# a.sort()
# print(a)
#
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# # remove the duplicate and sort the list
# basket = sorted(set(basket))
# print(basket)

# def power(x):
#     return x ** 2
#
# l = [power(x) for x in range(10)]
# l = [2, 3, -4, -5]
# res = ['positive' if i > 0 else 'not positive' for i in l]
# print(res)
#
# # given [3, 8, 9, 5] generate a new list, inside the list if the number is divisible by 3,
# # append True, else append False
# numbers = [3, 8, 9, 5]
# res = [True if i % 3 == 0 else False for i in numbers]

# l = [(i,j) for i in range(5) for j in range(i)]
# print(l)
# l = []
# for i in range(5):
#     for j in range(i):
#         l.append((i, j))

# homework
# solve the question use anything you learned so far
# given a list of numbers and an integer called target,
# find two numbers from the list such that they add up to target
# it's guaranteed in the list that such pair exists

# [3, 2, 1, 4, 5, 6] target=6
# return 1, 6
l = [3, 2, 1, 4, 5, 6]
target = 6
sorted(l)
left = 0
right = len(l) - 1
while left < right:
    tmp = l[left] + l[right]
    if tmp == target:
        print(l[left], l[right])
    elif tmp < target:
        left += 1
    elif tmp > target:
        right -= 1


# index = 0
# while index < len(l):
#     print(l[index])
#     index +=1
#
# def sum(list, target):
#     # for i in list:
#     #     for j in list:
#     #         if i + j == target:
#     #             print(i, j)
#     i = 0
#     while i < len(list):
#         j = i + 1
#         while j < len(list):
#             if list[i] + list[j] == target:
#                 print(list[i], list[j])
#             j += 1
#         i += 1
#
#
# def sum(list, target):
#     targetList = [tuple((i, j)) for i in list for j in list if i + j == target]
#     finalList = [tuple((sorted(i))) for i in targetList]
#     return sorted(set(finalList))
#
# print(sum([3, 2, 1, 4, 5, 6], 7))

# l = ['apple', 'orange', 'pear']
# res = []
# for i in l:
#     res.append((i, len(i)))
#
# res = [(i, len(i)) for i in l]