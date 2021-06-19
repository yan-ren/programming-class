'''
Given a non-empty list of integers, every element appear twice except for one.
Find that single one

nums = [1, 2, 2, 1, 4]
return 4

nums = [1, 2, 1]
return 2
'''

def notTwiceInList(lst):
    return int(''.join([str(num) for num in lst if lst.count(num) == 1]))

l = [1, 2, 3, 2, 3]
# print(l.count(3))

# idea 1, hint: use sort
# def find_single(l):
#     l.sort()
#     # [2, 2, 3]
#     index = 0
#     while index < len(l):
#         if index + 1 >= len(l) or l[index] != l[index+1]:
#             return l[index]
#         index += 2

# idea 2, hint: use dictionary
def find_single(l):
    dic = {}
    for i in l:
        dic[i] += 1

    for key, value in dic.items():
        if value == 1:
            return key

# def find_single(list):
#     list.sort()
#     index = 0
#     while index < len(list):
#         if index + 1 >= len(list):
#             return list[index]
#         elif list[index] != list[index+1]:
#             return list[index]
#         index += 2
#
#
# print(find_single([1,2,1,2,4]))
# print(find_single([1,2,4,1,2]))
'''
[1, 2, 1, 2, 4] -> [1, 1, 2, 2, 4]
'''

'''
Give a sorted list, delete all duplicates such that each element appears only once. Return the list sorted as well

example: [1, 1, 2, 2]
output: [1, 2]
'''

# single=0
# dict={}
# list=[1, 2, 1, 2, 3]
# for i in list:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
#
# for i,j in dict.items():
#     if j ==1:
#         single=i
# print(single)

# a^b
a = 1
b = 2
print(a**b)

# 2^3 == 2*2*2
# def power(base, exp):
#     result = 1
#     while exp > 0:
#         result = result * base
#         exp -= 1
#     return result
#
# print(power(2, 3))

def power_recursive(base, exp):
    if exp == 1:
        return base
    return base * power_recursive(base, exp - 1)

'''
Given a sorted list, delete all duplicates such that each element appears only once. 
Return the list sorted as well

example: [1, 1, 2, 2]
output: [1, 2]
'''
# luke
def sortList(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


def remove_dupl(list1):
    return list(set(list1))


# Jesse
def lol(z):
    tell = []
    for x in z:
        if x not in tell:
            tell.append(x)
    return tell
'''
Given a non-empty list of integers, every element appears once except for one element.
Find the element showed more than once

example: [1, 2, 3, 4, 5, 5]
return 5

example: [1, 1, 1, 1, 2]
return 1
'''

def findCount(element, list):
    count = 0
    for i in list:
        if element == i:
            count += 1
    return count


def dicFind(list):
    dic = {}
    for i in list:
        if i not in dic:
            x = findCount(i, list)
            dic[x] = i
    return dic


j = dicFind([1, 1, 2, 1, 5])
# {1: 3, 2: 1, 5: 1}
multupul_Dupl = 0
for keys, values in j.items():
    if keys > multupul_Dupl:
        multupul_Dupl = values

print(multupul_Dupl)


def find_duplicates(list):
    dic = {}
    for i in list:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for k, v in dic:
        if v > 1:
            return k






def findmorethanone(list):
    dic={}
    for i in list:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for i,j in dic.items():
        if j>1:
            return i


print(findmorethanone([1,2,2,3,4,5]))

'''
a^b 
base case: when b == 1: return a
recursive case: a^b = a*(a^(b-1))
                a^(b-1) = a*(a^(b-2))
                ...
                a^2 = a*a^1
   base case    a^1 = a
'''

'''
write a function that takes string as input, and print each character in reversed order
'''
'''
base case: when string has one character
recursive case:

"abcd" = "a" + "bcd"
"bcd" = "b" + "cd"
"cd" = "c" + "d"
'''
def print_reverse(str):
    if len(str) == 1:
        print(str)
    else:
        print_reverse(str[1:])
        print(str[0])

'''
given a list of number, write a recursive function to sum all elements in the list
base case: when list has only one element
recursive case: list[0] + sum(list[1:])

[1, 2, 2, 3] == [1] + [2, 2, 3]
[2, 2, 3] == [2] + [2,3]
[2, 3] == [2] + [3]
'''
def recursive_sum(list):
    if len(list) == 1:
        return list[0]
    return list[0] + recursive_sum(list[1:])