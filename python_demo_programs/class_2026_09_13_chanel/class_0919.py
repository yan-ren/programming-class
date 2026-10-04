# exercise: ask user for three number, how to find the largest
# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
# third = int(input('Enter third number: '))

# nested if statement
# if first > second:
#     if first > third:
#         print('First is largest')
#     else:
#         print('Third is largest')
# else:
#     if second > third:
#         print('Second is largest')
#     else:
#         print('Third is largest')
#
# if first > second and first > third:
#     print('First is largest')
# elif second > first and second > third:
#     print('Second is largest')
# else:
#     print('Third is largest')

i = 1
s = 0
while i <= 10:
    # print(i)
    s = s + i
    i += 1

print(s)

# 2 + 4 + 6 + ... + 20
# i = 2
# s = 0
# while i <= 20:
#     s = s + i
#     i += 2
# print(s)

# i = 1
# s = 0
# while i <= 20:
#     if i % 2 == 0:
#         s = s + i
#     i += 1
#
# print(s)

# i = 0
# while i < 10:
#     j = 1
#     while j < 3:
#         print(j)
#         j = j + 1
#     i += 1

# for

# list
name1 = 'Alice'
name2 = 'Bob'
name3 = 'Charlie'

names = ['Alice', 'Bob', 'Charlie']
names.append('David')
print(names)
print(names[0])

i = 0
while i < len(names):
    print(names[i])
    i += 1