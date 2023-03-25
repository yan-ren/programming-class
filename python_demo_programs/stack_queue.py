'''
use list as stack
'''
# s = []

# s.append(4)
# s.append(5)

# # pop function in list removes the last item in the list
# s.pop()

# # using python list append/pop function, we can achieve stack property


# '''
# use list as queue
# '''
# s = []
# s.append(4)
# s.append(5)

# # remove the value at index zero
# s.remove(0)
# s.remove(0)


# # python queue library
# from collections import deque
# q = deque()
# # add value to the right side of the queue
# q.append(2)
# q.append(3)
# # remove and return the value from the right side of the queue
# q.pop()

'''
Given a string s, remove the duplicate letters so taht every letter appears once,
also make sure the result is the smallest in lexicographical order among all possible results
don't reorder letter, letter can only be removed

s = "bcabc"

if
"bca"

"abc"

s = "cbacdcbc"
if
"acdb"

"abcd"

algorithm
1. create an empty stack. traverse on the string
2. for each char check if it's in the stack
2.1 if char is not in stack, and it's smaller than previous element in stack and those element are repeating in future,
we need to pop these elements and push char to stack
2.2 just push to stack

Example:
s = "bcabc"
last_dic = {"a": 2, "b": 3, "c": 4}

stack = []
[b]
[b, c]
pop c, pop b -> []
[a]
[a, b]
[a, b, c]

'''
def remove_duplicate(s):
    stack = []
    last_dic = {}

    for i in range(len(s)):
        last_dic[s[i]] = i
    
    for i in range(len(s)):
        if s[i] not in stack:
            while len(stack) != 0 and stack[-1] > s[i] and last_dic[stack[-1]] > i:
                stack.pop()
            
            stack.append(s[i])

    return ''.join(stack)


print(remove_duplicate("bcabc"))