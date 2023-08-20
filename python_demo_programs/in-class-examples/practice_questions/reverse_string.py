'''
Write a Python function to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''

'''
write a function:
input: string
output: string
'''
'''
[::-1]
[::-1] slicing from right to left == reverse a string
'''
def reverse_string(s):
    return s[::-1]


def reverse_string_1(s):
    result = ''
    index = len(s)-1
    while index >= 0:
        result += s[index]
        index -= 1
    return result


# print(reverse_string_1('abcde'))

'''
useful string methods
'''
greeting = 'hello world! hello'
# print(greeting[4])
# 'world' in greeting
# len(greeting)

# return the first find index of the substring
print(greeting.find('lo'))
print(greeting.replace('llo', 'y'))
print(greeting.startswith('Hell'))
print(greeting.lower())
print(greeting.upper())
print(greeting.isalpha())

'''
string <-> list
'''
s = 'ham,cheese,bacon'
# -> ['ham', 'cheese', 'bacon']
l = s.split(",")
print(l)

s = '2020-1-23'
l = s.split('-')
print(l)

'''
write a function which takes two string in data format 'yyyy-mm-dd'
return the earlier date
'''
def earlier_date(d1, d2):
    d1_list = d1.split('-')
    d2_list = d2.split('-')

    # compare the year
    if int(d1_list[0]) < int(d2_list[0]):
        return d1
    elif int(d1_list[0]) > int(d2_list[0]):
        return d2

    # compare the month
    if int(d1_list[1]) < int(d2_list[1]):
        return d1
    elif int(d1_list[1]) > int(d2_list[1]):
        return d2

    # compare the day
    if int(d1_list[2]) < int(d2_list[2]):
        return d1
    elif int(d1_list[2]) > int(d2_list[2]):
        return d2

    return d1


# print(earlier_date('2021-9-12', '2021-10-20'))
'''
list -> string
'''
# l = ['Eric', 'John', 'Michael']
# print(','.join(l))
age = 10
grade = 10
s = f'I am {age} years old in grade {grade}'
print(s)


'''
difference between tuple and list
- mutability(changeable)
mutable: you can change it after creation
immutable: you cannot change it afer creation
'''
l = [1, 2, 3, 4]
t = (1, 2, 3, 4)
print(type(l))
print(type(t))
print(t[0])
l[0] = 100
l.append(4)

# count the number of occurrences in a list
l.count(1)
# extend a list by appending all elements from another
l = [3, 1, 2, 4]
# l.sort()
l.reverse()
# l.extend([1, 2, 3])
# l.append([1, 2, 3])
print(l)




# def count_list(list, target):
#     count = 0
#     for number in list:
#         if number == target:
#             count += 1
#
#     return count

'''
write a python function, which takes a list of numbers(positive or negative, no zero)
return two list, first contains only positives and second contains only negatives
'''
