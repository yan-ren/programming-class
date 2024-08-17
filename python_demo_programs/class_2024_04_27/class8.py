# function/method
# print() input() int() randin() len() range()
import math


def print_welcome():
    name = input('What is your name:')
    print('Welcome', name)


# print_welcome()
# print_welcome()

def print_custom_welcome(msg):
    name = input('What is your name:')
    print(msg, name)


print_custom_welcome('Hello')
print_custom_welcome('Hi')


def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print('The distance is', distance)

# distance(1, 1, 2, 2, 1)
def sum(list):
    res = 0
    for value in list:
        res += value

    # print('Sum of list is', res)
    return res

sum([1, 2, 3, 1, 2, 3])

'''
exercise:

Write a python function which takes two list as input, compare which list has a bigger sum in total

[1, 2, 3, 4]
[2, 1, 5, 9]
'''
def compare_sum(list1, list2):
    sum_list1 = sum(list1)
    sum_list2 = sum(list2)
    if sum_list1 > sum_list2:
        print('list 1 is bigger')
    else:
        print('list 2 is bigger')


compare_sum([1, 2, 3], [2, 3, 4])
'''
https://github.com/loucadufault/420-LCU-05/blob/master/Assignment-2/A-2_instructions.pdf
'''