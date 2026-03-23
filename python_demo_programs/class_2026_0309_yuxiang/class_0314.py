'''
while loop
for loop
'''
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# exercise: calculate the sum of 1 to 100, e.g 1+2+3+...+99+100
i = 1
s = 0

while i <= 100:
    # print(i)
    s = s + i
    i += 1

print(s)

# exercise: calculate all the even sum of 1 to 100, 2+4+6+8+ ... + 100
i = 1
s = 0

while i <= 100:
    # print(i)
    if i % 2 == 0:
        s = s + i
    i += 1

print(s)

# exercise: ask user for a number, write a countdown program from given number

# i = 1
# while i < 10:
#     if i == 2:
#         break
#     print(i)
#     i += 1
#
# i = 1
# while i < 10:
#     if i == 2:
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 0
# while i < 4:
#     j = 0
#     while j < 3:
#         print(j)
#         j += 1
#     i += 1

i = 0
while i < 4:
    j = 0
    while j < 4:
        print('*', end='')
        j += 1
    print()
    i += 1

# print(2, end='')
# print(3)

'''
*
**
***
****
'''

# i = 0
# while i < 4:
#     j = 0
#     while j < i + 1:
#         print('*', end='')
#         j += 1
#     print()
#     i += 1

# print(list(range(3)))
# print(list(range(1, 5)))
# print(list(range(1, 6, 2)))

for i in range(3):
    print(i)

s = 'abc1234e'
for ch in s:
    print(ch)

numbers = [1, 2, 1, 4, 2, 5]
for num in numbers:
    print(num)

print(numbers[0])
numbers[0] = 100

s = 'abcd'
s[0] = 'w'

# exercise:
'''
given a list of number, find the largest and smallest number
given a list of number, find the sum and average
'''
numbers = [2, -1, 2, 5, -29, -10]
# largest = numbers[0]
# smallest = numbers[0]
#
# for num in numbers:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
#
# print(largest)
# print(smallest)

sum = 0
for num in numbers:
    sum += num

print(sum)
print(sum / len(numbers))
