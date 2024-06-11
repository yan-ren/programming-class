'''
Given a list of numbers, there is one number showed multiple times, find that number
list = [1, 2, 3, 4, 1]
number = 1
'''
'''solution 1
list = [1, 2, 3, 1, 4]
i = 0
duplicated = None
while i < len(list):
    j = i + 1
    while j < len(list):
        if list[i] == list[j]:
            duplicated = list[i]
        j += 1
        
    i += 1
'''

'''solution2
list = [1, 2, 3, 4, 1, 7]
seen = []

for value in list:
    if value not in seen:
        seen.append(value)
    else:
        print(value)
'''


'''Today: 
function/method
'''
def print_msg():
    print('welcome to the class')
    print('today is a good day')


print_msg()
# print_msg()
#
# def print_msg_name(name):
#     print(name, 'welcome to the class')
#
#
# print_msg_name('Tom')
#
# def print_msg_multiple_name(name1, name2):
#     print(name1, 'welcome to the class')
#     print(name2, 'welcome to the class')
#
#
# print_msg_multiple_name('Tom', 'Jerry')

'''
Write a function which takes a list as input and print the largest number
'''
def find_max(list):
    max = list[0]
    for value in list:
        if value > max:
            max = value

    print(max)


find_max([1, 2, 5, 3])
find_max([1, 2, 5, 3, 10])

'''
Exercise: write a function that takes two lists as input, 
print a single list which is the combination of the two inputs

list1: [1, 2, 3]
list2: [2, 3, 4]

print: [1, 2, 3, 2, 3, 4]
'''
def merge_list(list1, list2):
    res = []
    for value in list1:
        res.append(value)

    for value in list2:
        res.append(value)

    return res

'''
Exercise: write a function that takes a string as input, and print the string reversely

input: 'abc'
print: 'cba'
'''
def reverse_print(text):
    new_text = ''
    index = len(text) - 1
    while index >= 0:
        new_text = new_text + text[index]
        index -= 1

    return new_text
