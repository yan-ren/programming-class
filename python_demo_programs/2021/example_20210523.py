'''
reverse a string

given a string, write a function that returns the reversed string
e.g "abc" -> "cba"
"hello" -> reverse("ello") + "h"
reverse("ello") -> reverse("llo") + "e"
reverse("llo") -> reverse("lo") + "l"
reverse("lo") -> reverse("o") + "l"
reverse("o") -> "o"
'''
# def reverse_string(word):
#     if len(word) == 1:
#         return word
#     else:
#         return reverse_string(word[1:]) + word[0]

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(5))
'''
fib(n) = fib(n-1) + fib(n-2)
fib(n-1) = fib(n-2) + fib(n-3)
fib(n-2) = fib(n-3) + fib(n-4)
'''

'''
Write a Python program of recursion list sum
e.g. [1, 2, [3,4], [5,6]]
return 21

base case: when element is single value, just add to the sum
recursive case: when element is a list, call function get the sum of the list
'''

'''
Given a string, how to print the string in reversed order, one line per char
given "abc"

c
b
a

str = "abcde" -> "abcd" + "e"

"abcd" = "abc" + "d"

"abc" = "ab"+ "c"

"ab" = "a" + "b"

"a" = print("a")

'''
# def reverse_print(str):
#     if len(str) == 1:
#         print(str[0])
#         return
#     else:
#         print(str[len(str) - 1])
#         reverse_print(str[:len(str)-1])
#
# reverse_print("abcd")

'''
Write a function takes string as input and return a new reversed string
"abc" 
return "cba"
'''

def reverse_string(str):
    new_str = ""
    length = len(str) -1
    while length >= 0:
        new_str += str[length]
        length -= 1

'''
base case: "a" -> "a"
recursive case: 
reverse("abcd") -> reverse("bcd") + "a"
reverse("bcd") -> reverse("bc") + "d"
reverse("bc") -> reverse("c") + "b"
reverse("c") -> "c"
'''

'''
Write a Python program to get the top three items in a shop
Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

item4 55
item1 45.5
item3 41.3
'''
data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
values = list(data.values())
values.sort(reverse=True)
top_three = values[:3]
print(top_three)
for keys, values in data.items():
    if values in top_three:
        print(keys)

# def find_largest(source):
#     dic = {}
#
#     for keys, values in source.items():
#         for key, value in source.items():
#             if value > values:
#                 dic[key] = value
#
#     return dic
#
#
# a = find_largest({'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24})
# print(a)
# x = a.items()
# first_three_items = list(x)[:3]
# for i in first_three_items:
#     print(i)


"""
Give a sorted list, delete all duplicates such that each element appears only once. Return the list sorted as well

example: [1, 1, 2, 2]
output: [1, 2]
"""