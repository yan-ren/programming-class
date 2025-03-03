numbers = [2, 1, 3, 5]

# index = 0
# while index < len(numbers):
#     print(numbers[index])
#     index += 1
print(numbers)
for index in range(1, len(numbers)):
    numbers[index] += 1
    # print(numbers[index])
print(numbers)

# print(numbers)
# for num in numbers:
#     num += 1
#
# print(numbers)
# index = len(numbers) - 1
# while index >= 0:
#     print(numbers[index])
#     index -= 1

range(4)    # 0, 1, 2, 3
range(1, 4) # 1, 2, 3
range(1, 5, 2) # 1, 3

numbers = [0, 1, 2, 3, 4, 5]
for i in range(1, len(numbers), 2):
    print(numbers[i])


new_numbers = []
index = 1
while index < len(numbers):
    print(numbers[index])
    new_numbers.append(numbers[index])
    index += 2

numbers = [-2, -2, 1, 3, -6]
# positive = []
# for num in numbers:
#     if num > 0:
#         positive.append(num)
#
# print(positive)

# max_number = numbers[0]
# second_max = numbers[0]
#
# for num in numbers:
#     if num > max_number:
#         second_max = max_number
#         max_number = num
#     elif num > second_max:
#         second_max = num
#
# print(max_number)

# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()

matrix = [[1, 1, 1],
          [-1, 0, 2],
          [1, 2, 3]]
# print(len(matrix))
# print(matrix[0][1])
# for row in matrix:
#     row_sum = 0
#     for col in row:
#         row_sum += col
#     print(row_sum)
row = len(matrix)
col = len(matrix[0])

for i in range(col):
    col_sum = 0
    for j in range(row):
        col_sum += matrix[j][i]

    print('The total in column', i+1, "is", col_sum)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
montreal = ['MONTREAL TRUDEAU (AIRPORT)', 'QC', -9.2, -8.0, -2.0, 6.2, 13.9 , 19.0 , 21.7 , 20.6 , 16.0 , 8.9, 2.3, -5.0]
for index in range(len(months)):
    # The monthly average temperature in Montreal in Jan was -9.2.
    print('The monthly average temperature in Montreal in', months[index], 'was', montreal[index + 2])

a = 'hello'
b = 'Hello'
print(a > b)