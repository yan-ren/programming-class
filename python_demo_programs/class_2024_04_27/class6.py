'''
list
'''
name = 'Tom'

names = ['Tom', 'Jerry', 'Peter']
# print(names)
# print(names[0])
# # print(names[3])
#
# print(len(names))
# max index = number of element - 1

# index = 0
# while index < len(names):
#     print(names[index])
#     index += 1

numbers = [1, 2, 1, 4, 2, 7, 4]
# sum = 0
# index = 0
#
# while index < len(numbers):
#     sum += numbers[index]
#     index += 1
#
# print(sum)

'''
list can be used with for loop
'''
sum = 0
for num in numbers:
    sum += num

print(sum)

numbers = [1, 2, 3, 4]
numbers.append(10)
print(numbers)

del numbers[1]
print(numbers)

# insert a value at given index
numbers.insert(1, 100)
print(numbers)

