from multiprocessing.sharedctypes import Value
from operator import attrgetter
from queue import PriorityQueue

'''
Priority Queue

queue: ADT, first in first out

- implementation: 
    - python queue
    - python list
    - linked list [ ]->[ ]->[ ]

priority queue:
- ADT, elements allows arbitrary insertion, but each element has priority
when remove the element, element with first priority gets removed

2:1
1:3
4:2
d:5
e:4

remove() -> d
remove() -> 

- Binary tree -> heap -> priority queue
'''

# i = 0
# while i < 10:
#     j = 0
#     while j < i + 1:
#         print("*", end='')
#         j += 1
#     i += 1
#     print() 

i = 0
while i < 10:
    j = 0
    while j < i + 1:
        print("*", end='')
        j += 1
    i += 1
    print() 
'''
*
**
***
****
*****
******
*******
********
*********
**********


**********
*********
********
*******
******
*****
****
***
**
*
'''
# by default, printing goes to the next line after it's done
# print(1, end='')
# print(2)

'''
palindrome

A palindrome is a word that reads the same in the forward
and reverse direction. 
e.g. 
bob
kayak
racecar
mom
noon
level

string


'''
# s = "kayak"
# index = 0
# while index < len(s):
#     print(s[index])
#     index += 1
'''
inside loop
compare first character with the last character
then continue to compare second with second last
if any pair doesn't match, its not palindrome
if all match, it's palindrome

0 1 2 3 4
k a y a k

index = 0
compare with index 4

5      - 0     - 1 = 4
len(s) - index - 1

index = 1
compare with 3
len(s)-index-1 = 5 - 1 - 1 = 3
'''
while True:
    s = input("enter a string to check if it is palindrome: ")
    index = 0
    palindrome = True
    while index < len(s) / 2:
        if s[index] != s[len(s) - index - 1]:
            palindrome = False
            break
        index += 1

    if palindrome:
        print("it is palindrome")
    else:
        print('it is not palindrome')



