# stack and queue

# stack, LIFO
stack = []

# push/add value
stack.append(0)
stack.append(10)
stack.append(20)

print(stack.pop()) # remove the last value -> LIFO

# check if stack is empty
if stack:
    print(stack.pop())


# exercise: reverse a string, using a stack
stack = []
s = 'abcdef'

for ch in s:
    stack.append(ch)

s_reversed = ''
while stack:
    s_reversed += stack.pop()

print(s_reversed)

# exercise: backspace editor, process # as deletion: 'ab#c' becomes 'ac'
text = 'ab#c'
stack = []
for ch in text:
    if ch == '#':
        if stack:
            stack.pop()
    else:
        stack.append(ch)

print(''.join(stack))

# exercise: check valid brackets, check nesting of () [] {}, valid: [(())], invalid : ([)]