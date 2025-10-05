'''
Given a string containing just the characters '(', ')', '{', '}', '[', and ']',
determine if the input string is valid. An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

# Example
print(isValid("()"))  # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))  # Output: False
'''
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            open = None
            if stack:
                open = stack.pop()
            if mapping[char] != open:
                return False
        else:
            stack.append(char)
    # if len(stack) == 0:
    #     return True
    # else:
    #     return False

    return not stack


queue = []
queue.append('a')
queue.append('b')
queue.pop() # not correct, this is the usage for stack
queue.pop(0) # correct, this pop the first value in the list, which follow the FIFO order
'''
python list can be used both as stack or queue,
'''

# from collections import deque
#
# q = deque()
# q.append('a')
# q.append('b')
#
# print(q.popleft())
# print(q.popleft())

'''

Given a number N, generate binary numbers from 1 to N using a queue.

1: 1
2: 10
3: 11
4: 100
5: 101

Example:
Input: N = 5
Output: ['1', '10', '11', '100', '101', '110', '111']

Idea
You start with 1, and for each number, you generate the next two by appending 0 and 1.
For 1, appending 0 and 1 gives 10 and 11.
For 10, appending 0 and 1 gives 100 and 101, and so on, until you reach N.

'''