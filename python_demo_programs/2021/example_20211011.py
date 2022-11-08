'''
Given a list of integers, move all 0's to the end of list while maintaining the relative order of the non-zero elements

nums = [0,1,0,3,12]
[1,3,12,0,0]
'''

# nums = [0, 1, 0, 3, 1, 2]

# output_nums = []
# for i in nums:
#     if i > 0:
#         output_nums.append(i)

# for j in nums:
#     if j == 0:
#         output_nums.append(j)

# print(output_nums)


# def move_zero(list):
#     output_nums = []
#     zeros = []
#     for i in list:
#         if i > 0:
#             output_nums.append(i)
#         else:
#             zeros.append(i)

#     output_nums.extend(zeros)


# a = [1, 2, 3]
# b = [4, [5, 6]]
# # a.append(b)
# # print(a)

# a.extend(b)
# print(a)

# get the nth fibnacii number
def fib(n):
    # for the first and second number just return the value
    if n==1 or n==2:
        return 1

    # if n is bigger than 2
    return fib(n-1)+fib(n-2)

# given a non-negative int n, return the sum of its digits using loop
def sum_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10  # get the right most digit
        n = n // 10     # remove the right most digit
        sum += digit

    return sum

def sum_digits_recursive(n):
    if n < 10:
        return n
    return sum_digits_recursive(n // 10) + n % 10
'''
Write a Python program to print all unique values in a dictionary.
Sample Data : {{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}}
Expected Output : Unique Values: {'S002', 'S007', 'S009'}
'''

'''
Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary
Assume each key contains a list as value, where the list has two elements

Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ace
adf
bce
bdf

['a', 'b']

['c', 'd']
'''

# d = {'1':['a','b'], '2':['c','d']}
#
# di={'1':['a','b'],'2':['c','d'], '3': ['e','f']}
# l=[]
# for key,value in di.items():
#     l.append(value)
# for i in l[0]:
#     for j in l[1]:
#         print(i+j)


sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

def convert_to_list(sample_data):
    list1 = []
    for index in sample_data:
        for value in index.values():
            list1.append(value)
    return list1


def find_unique(list1):
    output = []
    nlist = convert_to_list(list1)
    list1 = set(nlist)
    for i in list1:
        nlist.remove(i)
        if i not in nlist:
            output.append(i)

    return output

print(find_unique([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VII":"S007"}]))

d = {"V":"S001", "VI": "S001", "VII":"S005"}
# loop through d and put each values into a set, then print set
def print_duplicate_values(d):
    s = set()
    # s = {}
    # len(s)

    for key, value in d.items():
        s.add(value)
    print(s)

print_duplicate_values(d)

'''
5 3 2 1 4 6

bubble sort
1 2 3 4 5 6
'''
# def bubble_sort(n):
#     sorted = False
#     while not sorted:
#         sorted = True
#         index = 0
#         while index < len(n) - 1:
#             if n[index] < n[index+1]:
#                 # swap n[index] with n[index+1]
#                 n[index], n[index+1] = n[index+1], n[index]
#                 sorted = False
#
#     return n
#
#
# def reverse(string):
#     if len(string) == 1:
#         return string
#     return string[-1] + reverse(string[0:len(string)-2])

'''
reverse a string using non-recursive and recursive solution
given "abc"
reversed "cba"
'''
def reverse(string):
    if len(string) == 1:
        return string
    return string[-1] + reverse(string[0:len(string)-1])

print(reverse("abcde"))
