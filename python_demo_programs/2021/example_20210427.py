# def calculation():
#     global place
#     place = "Cape Town" # change global variable "place"
#     global name
#     name = "John" # global variable
#     print(place)
#
#
# place = "Berlin" # global variable
# print(place)
# calculation()
# print(place)
# print(name) # try print global variable "name"

def welcome(msg):
    print(msg)
    welcome(msg)

welcome("hello")

'''
Given an integer list, 
find the contiguous sublist (containing at least one number) which has the largest sum and return its sum.

input = [-2,1,-3,4,-1,2,1,-5,4]
        [-2, 1, -2, 4, 3, 5, 6, 1, 5]
sublist [4,-1,2,1] gives the largest sum 6, return 6

Input: nums = [5,4,-1,7,8]
output: 23
'''
# def maxSubArray(nums):
#     max = nums[0]
#     i = 0
#     while i < len(nums):
#         if nums[i] > max:
#             max = nums[i]
#
#         index_sum = nums[i]
#         j = i + 1
#         while j < len(nums):
#             index_sum += nums[j]
#             if index_sum > max:
#                 max = index_sum
#             j += 1
#         i += 1
#     return max
#
l = [-2,1,-3,4,-1,2,1,-5,4]
# print(maxSubArray(l))

# def maxSubArray(nums):
#     store = []
#     store.append(nums[0])
#     max = nums[0]
#
#     index = 1
#     while index < len(nums):
#         if store[index - 1] > 0:
#             store.append(nums[index] + store[index-1])
#         else:
#             store.append(nums[index])
#
#         if store[index] > max:
#             max = store[index]
#         index += 1
#
#     return max
#
# print(maxSubArray(l))

def counter(n):
    while n > 0:
        print(n)
        n -= 1


def counter_recursive(n):
    if n == 0:
        return
    else:
        print(n)
        counter_recursive(n-1)

counter_recursive(3)

'''
Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. If the last word does not exist, return 0.

example:
s = "Hello World"
length = 5

s = "good morning Tom"
length = 3

s = "welcome"
length = 7
'''

def add(n):
    if n <= 1:
        return n
    else:
        return n + add(n-1)

print(add(4))


def max_sublist(l):
    max = l[0]
    i = 0
    while i < len(l):
        if l[i] > max:
            max = l[i]
        sum = l[i]
        j = i + 1
        while j < len(l):
            sum = sum + l[j]
            if sum > max:
                max = sum
            j += 1
        i += 1
    return max
