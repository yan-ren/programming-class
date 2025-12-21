'''
list
'''
# numbers = [1, 2, 1, 3, 2, 4, 1, 2, 1]
# print(numbers)
#
# numbers.append(10)
# print(numbers)
# print(numbers[6])
#
# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1

numbers = [-1, -2, -1, -4, -20, -2]
# sum = 0
#
# index = 0
# while index < len(numbers):
#     sum += numbers[index]
#     index += 1
#
# print(sum / len(numbers))

# find the largest value from the list
max = numbers[0]
index = 0
while index < len(numbers):
    if numbers[index] > max:
        max = numbers[index]
    index += 1

