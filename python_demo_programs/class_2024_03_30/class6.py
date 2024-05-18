# list = [1, 3, 2, 5, 1, 2]
# print(list[0])
# print(list[1])
#
# list[0] = 10
#
# print(list)

# while loop to access all elements
# index = 0
# while index < len(list):
#     print(list[index])
#     index = index + 1

# only iterable can be placed after 'in' keyword
# for value in list:
#     print(value)
#
#
# s = 'abcdef'
# for c in s:
#     print(c)
# range(10) -> 0, 1, 2, ... 9
# for i in range(10):
#     print(i)

# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# import turtle
#
# window = turtle.Screen()
# window.setup(800, 600)
# alex = turtle.Turtle()
# number_of_triangle = 72
# for i in range(number_of_triangle):
#     for color in ['yellow', 'red', 'purple']:
#         alex.color(color)
#         alex.forward(100)
#         alex.left(120)
#
#     alex.left(360/number_of_triangle)
#
# window.exitonclick()

# words = ['abc', 'b', 'bbbc', 'abcdefs']
# # how to find the longest string from the list
# longest_word = ''
# for s in words:
#     if len(s) > len(longest_word):
#         longest_word = s
#
# print(longest_word)

'''
given a list of number, positive and negative
create a new list only with positive value
'''
# numbers = [1, 2, -1, 4, -2]
# new_numbers = []
#
# for value in numbers:
#     if value > 0:
#         new_numbers.append(value)
#
# print(new_numbers)

'''
given a list of values, reverse the list
'''
numbers = [1, 2, 3, 4]
reversed = numbers
# [4, 3, 2, 1]
# reversed = []
#
# i = len(numbers) - 1
# while i >= 0:
#     reversed.append(numbers[i])
#     i = i-1

index = 0
while index < len(numbers)/2:
    # swap numbers[index] with numbers[len(numbers)-1-index]
    tmp = numbers[index]
    numbers[index] = numbers[len(numbers) - 1 - index]
    numbers[len(numbers) - 1 - index] = tmp
    index += 1


'''
given two list of number, check if list contains the same numbers
list1 = [1, 3, 2]
list2 = [2, 3, 1]
they have the same numbers

list1 = [1, 3]
list2 = [1]
they have different numbers
'''
list1 = [1, 3, 2]
list2 = [2, 3, 1]
same = True

if len(list1) == len(list2):
    for value in list1:
        if list1.count(value) == list2.count(value):
            same = False
    same = True

list = [1, 1, 2, 2, 2, 3]
print(list.count(100))
print(list.index(100))
if 100 in list:
    print(list.index(100))

