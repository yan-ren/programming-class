# import pprint
# from re import T
# from textwrap import indent


# nums=[-3,-1,0,2,4]
# res=[]
# head=0
# tails=len(nums)-1
# while head <= tails:
#     print(head, tails)
#     if abs(nums[head]) < abs(nums[tails]):
#         res.insert(0,abs(nums[tails]))
#         tails-=1
#     else:
#         res.insert(0,abs(nums[head]))
#         head+=1
# res.insert(0,0)
# print(res)


# '''
# given a sorted list numbers, calculate the absolute value for each number and 
# return the result as a sorted list

# e.g.
# [-3, -2, 0, 10, 12]

# [0, 2, 3, 10, 12]

# can you think about another solution that doesn't use list.sort()
# hint: input is sort

# solution1:
# find the first non-negative from the left, initialize two index, left and right

# solution2:
# initizlie two index, left and right
# '''

# def sorted_abs_list(nums):
#     left = 0
#     right = len(nums) - 1
#     res = []
#     while left <= right:
#         if abs(nums[left]) > abs(nums[right]):
#             res.insert(0, abs(nums[left]))
#             left += 1
#         else:
#             res.insert(0, abs(nums[right]))
#             right -= 1
#     return res

# print(sorted_abs_list([-3, -2, 0, 10, 12]))




# d1 = {"A": 1, "B": 2}
# d2 = {"C": 3}
# d4 = {"D": 4}

# d3 = {**d1, **d2, **d4}
# print(d3)

# # user underscore to separate zeros to improve readability
# n = 1000_00_0
# n += 1

# pprint.pprint(d3, width=2)

# # string strip
# # remove unwanted charaters from string
# str = "++hel++lo++"
# str = str.strip('+')
# str.lstrip()
# str.rstrip()
# print(str)

# print(str * 5)
# str.split(' ')


# t = [1, 2, 3]
# a, *b = t
# print(a)
# print(b)

# '''
# given a list of numbers, print the number of positive numbers and negative numbers

# [1, 2, 1, -2, -2]
# 3
# 2
# '''
# l = [1, 2, 3, -4, -4, 0, 2.5]
# count_pos = 0
# count_neg = 0

# for i in l:
#     if i > 0:
#         count_pos += 1
#     if i < 0:
#         count_neg += 1

# print(count_pos)
# print(count_neg)


# '''
# range
# '''
# print(list(range(4)))
# print(list(range(-2, 4)))
# print(list(range(4, -1, -1) ))


# def function1(msg):
#     print(msg)


# function1("class")
# function1("hello")
# function1()

# '''
# convert the previous practic: find largest value in list
# into a function
# '''
# def lol(numbers):
#     largest = numbers[0]
#     for n in numbers:
#         if n > largest:
#             largest = n

#     return largest

# res = lol([1, 3, 4, 5, 6])
# lol([1, 2, 3, 4, 5, 6])
# print(res)

# # def function1():
# #     print('inside function1')

# # def function2():
# #     function1()
# #     print('inside function2')

# # function2()

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# for i in range(100):
#     if is_even(i):
#         print(i)


# '''
# write a function that checks is any number in the list is duplicated
# '''

# def duplicated_list(l):
#     i = 0
#     while i < len(l):
#         j = i + 1
#         while j < len(l):
#             if l[i] == l[j]:
#                 return True
#             j += 1
#         i += 1

#     return False

# print(duplicated_list([1, 2, 3, 1]))
# print(duplicated_list([1, 2, 3]))


def lol(numbers):
    
    largest = numbers[0]
    smallest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n

    # print(largest)
    # print(smallest)

    return smallest, largest

smallest, largest = lol([1, 2, 3])
print(smallest)
print(largest)
