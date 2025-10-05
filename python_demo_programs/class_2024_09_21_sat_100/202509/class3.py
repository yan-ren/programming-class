'''
Data Structure

list - list
tuple - array
dictionary - map
set

stack
ADT: Abstract Data Structure

queue
'''

# use list to perform like a stack
# stack = []
#
# stack.append('A')
# stack.append('B')
# stack.append('C')
# print(stack.pop()) # C
# print(stack)
# print(stack.pop()) # B
# print(stack.pop()) # A
#
# if len(stack) != 0:
#     stack.pop()

# s = 'abcde'
# stack = []
#
# for ch in s:
#     stack.append(ch)
#
# s_new = ''
# while len(stack) != 0:
#     s_new += stack.pop()

'''
Valid Parentheses

Given a string containing just the characters '(' and ')', determine if the input string is valid. 
An input string is valid if every open parenthesis is closed by a matching closing parenthesis, 
and open parentheses are closed in the correct order.

valid: '()()'
invalid: '(()'

valid: '(())'
invalid: ')(()'
'''
def is_valid(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')' and len(stack) != 0:
            stack.pop()
        else:
            return False

    if len(stack) > 0:
        return False

    return True

print(is_valid('()()'))
print(is_valid('(()'))