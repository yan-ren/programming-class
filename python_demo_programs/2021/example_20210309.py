x = [1, 2, 3]
# list value [1, 2, 3] is stored in object,
# and this is mutable object

'''
Square of sorted list
Given an integer list sorted in increasing order, 
return an list of the squares of each number sorted in increasing order

Input: [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
'''
# def method():
#     a = 1
#     print(locals())
#
# method()
# print(globals())
input = [-4, -1, 0, 3, 10]
i = 0
index = 0
# find the index of first positive number
# variable index is the index of first positive number
# while index < len(input):
#     if input[index] >= 0:
#         break
#     index += 1
# i = index - 1
# output = []
# while i >= 0 and index < len(input):
#     if input[i]**2 > input[index]**2:
#         output.append(input[index]**2)
#         index+=1
#     else:
#         output.append(input[i]**2)
#         i-=1
#
# while i >= 0:
#     output.append(input[i]**2)
#     i-=1
#
# while index < len(input):
#     output.append(input[index]**2)
#     index+=1

# x = 3
# if x > 0:
#     y = True
# print(y)
# print(globals())


class MyClass:
    num = 1

    def greet(self):
        return "Hello world!"

list=[-6,-4,5,2,1,0,3]
i = 0
while i < len(list):
    if list[i] < 0:
        list[i] = -1*list[i]
    i+=1

list.sort()
i = 0
while i < len(list):
    list[i] = list[i] ** 2
    i+=1
