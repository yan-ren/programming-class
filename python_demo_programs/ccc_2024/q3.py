# number_num = int(input())
# list_numbers = []
#
# for _ in range(number_num):
#     list_numbers.append(int(input()))
#
# new_list = sorted(list(set(list_numbers)), reverse=True)
#
# third = new_list[2]
#
# count = 0
# for number in list_numbers:
#     if number == third:
#         count += 1
#
# print(third, count)

N = int(input())

list_days = []
list_count = [0] * 5
# print(list_count)

for _ in range(N):
    line = input() # 'Y.Y..'
    for index in range(len(line)):
        if line[index] == 'Y':
            list_count[index] += 1

# print(list_count) # Obtain a list of all numbers

maximum = max(list_count)

result = []
for index in range(len(list_count)):
    if list_count[index] == maximum:
        result.append(str(index + 1))

# [1, 3]
print(','.join(result))
