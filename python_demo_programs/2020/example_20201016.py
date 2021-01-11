# homework
# write a python function takes two lists as input, check if one list contains another list
# [1, 2, 3] [1, 2] -> true
# [1] [1, 2, 3] -> true
# [1, 2] [1, 3] -> false
list1 = [1, 2, 3]
list2 = [1, 2]

def contains(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True

# def contains(list1, list2):
#     return list1 in list2 or list2 in list1
#
#
# # test1
# print(contains([1, 2, 3], [1, 2]))
# # test2
# print(contains([1], [1, 2, 3]))
# # test3
# print(contains([1, 3], [1, 2]))
#
# greeting = 'hello'
# greeting_list = [1, 2, 3]
# greeting.count('he')
# greeting_list.count(1)

# index
# greeting[0]
# greeting_list[0]

# mutable vs immutable
# greeting_list[0] = 10

# 'hello' -> ['h', 'e', 'l', 'l', 'o']

# s = 'helloworld'
# l = list(s)
# print(l)

# exercise: write a function that convert a string to list
# e.g. 'Hello' -> ['H', 'e', 'l', 'l', 'o']
# do not use list()

def split(str):
    l = []
    for s in str:
        l.append(s)
    return l

# exercise: write a function that coverts a list to string
# e.g. ['H', 'e', 'l', 'l', 'o'] -> 'Hello'

def join(list):
    s = ''
    for l in list:
        s += l

    return s

print(join(['a', 'b', 'c']))
# list = ['a', 'b', 'c']
# str = ':'.join(list)
# print(str)

# homework: write a function takes two strings in date format 'xxxx-xx-xx'
# returns the earlier date
# e.g. input: '2020-02-02' '1990-12-13'
# return '1990-12-13'
def compare_date(date1, date2):
    date1_list = date1.split('-') # '2020-02-02' -> ['2020', '02', '02']
    date2_list = date2.split('-') # '1993-12-12' -> ['1993', '12', '12']

    # compare the year then month then day
    if int(date1_list[0]) > int(date2_list[0]):
        return date2
    elif int(date1_list[0]) < int(date2_list[0]):
        return date1

    # compare the month
    if int(date1_list[1]) > int(date2_list[1]):
        return date2
    elif int(date1_list[1]) < int(date2_list[1]):
        return date1

    # compare the day
    if int(date1_list[2]) > int(date2_list[2]):
        return date2
    elif int(date1_list[2]) < int(date2_list[2]):
        return date1

    return None
