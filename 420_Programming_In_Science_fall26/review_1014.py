
numbers = [[2, 1], [2, 3]] # 2d list / nested list, matrix
sum = 0
for number in numbers:
    for num in number:
        sum += num

print(sum)


# range(3)
# for i in range(3):
#     print(i)
#
# # range(3, 6)
# for i in range(3, 6):
#     print(i)
#
# # range(3, 10, 2)
# for i in range(2, 10, 2):
#     print(i)
#
# for i in range(0, len(numbers), 2):

# v = ['red', 'green', 'blue']
# n = 0
#
# for w in v:
#     n += len(w)
#
# print(n, w)

v = ["red", "orange", "green", "yellow", "blue", "black", "cyan"]
for i in range(1, len(v)): # for i in range(1, 7)
    j = i
    while j > 0 and v[j - 1] > v[j]:
        v[j - 1], v[j] = v[j], v[j - 1]
        j -= 1
print(v)

'''
i = 1, 2, 3, 4, 5, 6

when 
i = 1
j = 1

while j > and v[0] > v[1] -> false

when
i = 2
j = 2

while 2 > 0 and v[1] > v[2]:
    v[1], v[2] = v[2], v[1] # ['red', 'green', 'orange', 'yellow', 'blue', 'black', 'cyan']
    j -= 1
    
while 1 > 0 and v[0] > v[1]:
                            ['green', 'red', 'orange', 'yellow', 'blue', 'black', 'cyan']
                            
while
i = 3
'''

v = [1, 2]

v[0], v[1] = v[1], v[0]
print(v)

i = 0
while i < 1000:
    i += 1

# for
# string
# list
# range
# in is a keyword, only a certain thing can be put after 'in' keyword
for i in range(-5, 100):
    print(i)
# range works similiar like a list of numbers

s = 'abcd'
# for i in s:

# l = [1, 2, 3, 4]
# for x in ls:

def my_sqrt(x, error):
    y = x

    while abs(y**2 - x) > error:
        y = (y + x / y) / 2

    return y

print(my_sqrt(2, 0.01))

def pell(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    p_n_1 = 0
    p_n_2 = 1
    p_n = 0
    result = [p_n_1, p_n_2]
    while n >= 2:
        p_n = 2 * p_n_1 + p_n_2
        result.append(p_n)
        p_n_2 = p_n_1
        p_n_1 = p_n
        n -= 1

    return result