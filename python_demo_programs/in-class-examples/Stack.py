# class Stack():
#
#     def __init__(self):
#         self.data = []
#
#     def pop(self):
#         val = self.data[len(self.data) - 1]
#         del self.data[len(self.data) - 1]
#         return val
#
#     def push(self, data):
#         self.data.append(data)
#
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

'''
balanced brackets
[()]{}{[()()]()}

unbalanced brackets
[(])
'''




'''
You are given a list of integers and n queries. In each query, you are given an integer.

Your task is to find the minimum index greater than given integer, such that
sum of digits of integers is greater than the sum o

[5, 2, 3, 4, 1]

given 2
'''

'''
find all values in a list that are greater than all elements to their right

given list [10, 4, 6, 3, 5]

stack = [10, 6, 5]
'''






'''
create a stack

loop the given list
    if last value in stack is smaller than the current value in list, remove the value from the stack
    else add this value to stack

stack contains your answer
'''

given = [10, 4, 6, 3, 5]
s = []
for i in given:
    while len(s) > 0 and i > s[len(s) - 1]:
        s.pop()

    s.append(i)

print(s)
'''
source = "facebook"
target = "back"
target = "cake book"
'''

'''
Stack
'''
# s = []
# s.append(1)
# s.append(2)
# s.append(20)
#
# print(s.pop())
# print(s)
#
# print(s.pop())
# print(s)

'''
reverse a string using stack
'''

s = []
string = 'hello'

for letter in string:
    s.append(letter)

i = 0
while i < len(string):
    print(s.pop())
    i+=1

'''
Given an integer list nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

challenge: solve this problem without creating new list
'''

'''
Balanced brackets in an expression

given a string contains brackets 
"()()()"
"(())"
"()()(())"
"(()())"

not in pair
"(()"
"))"
'''
'''
define a stack
loop through the string
    1. if the current character is open brackets, push it to stack
    2. if the current character is closed bracket, then pop one character from stack,
    if the popped character is the matching bracket, then continue the loop, if not matching,
    then the string is not matched
after the loop, if stack is empty, then string is balanced
'''
'''
Given an expression string exp, 
write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” 
are correct in exp.

Input: exp = “[()]{}{[()()]()}” 
Output: Balanced

Input: exp = “[(])” 
Output: Not Balanced 
'''

'''
queue

queue is very similar as stack but it is first in first out
'''

# create a queue using list
q = []
q.append(1)
q.pop(0) # remove the index 0

import queue
q = queue.Queue()
q.put(1)
q.put(2)
print(len(q))






stack = []
stack.append(1)
stack.append(2)

# pop() function in the list remove the last value
print(stack.pop())

from queue import Queue
q = Queue()
q.put(1)
q.put(2)

# remove the value from queue
print(q.get())
print(q.get())


s = "abcd"

print(list(s))