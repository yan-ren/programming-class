'''
Square of sorted list
Given an integer list sorted in increasing order,
return an list of the squares of each number sorted in increasing order

Input: [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
'''
# input = [-4, -1, 0, 3, 10]
# output = []
#
# for i in input:
#     output.append(i**2)
#
# output.sort()
# # for a given value, if it's closer to the zero, its square is smaller.
# # to find a such value,
# # first find out the largest negative and smallest positive value
#
# def square_of_sorted(l):
#     # find out the index of largest negative and smaller postive
#     negative, positive = 0
#     index = 0
#     while index < len(l):
#         if l[index] > 0:
#             positive = index
#             break
#         index+=1
#     negative = positive - 1
#     output = []
#     while negative >= 0 and positive < len(l):
#         if l[negative]**2 > l[positive]**2:
#             output.append(l[positive]**2)
#             positive += 1
#         else:
#             output.append(l[negative]**2)
#             negative -= 1
#
# #   put the rest of values into the output
#     while negative >= 0:
#         output.append(l[negative]**2)
#         negative -= 1
#     while positive < len(l):
#         output.append(l[positive]**2)
#         positive += 1
#
#     return output
def method2():
    x = 20

def method1():
    method2()
    x = 2

x = 1
x = 100
method1()

'''
given a string and two numbers that represent the string index
return a new string with the character swapped at the index
e.g.
input: "abcde" 1 2
expect: "acbde"

input: "abcde" 0 4
expect: "ebcda"
'''
s = 'abcde'
l = list(s)
print(l)
l[0], l[1] = l[1], l[0]
s = ''.join(l)
print(s)






