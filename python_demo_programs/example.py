# print(5 + 5)
# print((9 + 5) % 12 + 1)
#
# print((1 - 5) % 12) # 1-5+12

# months = ["Jan", "Feb", "Mar", "Apr", "May",
#           "Jun", "Jul", "Aug", "Sep", "Oct",
#           "Nov", "Dec"]
#
# start_index = months.index('Feb')
# next_index = (start_index + 5) % 12
# print(months[next_index])

# month = input('Enter the month:')
# month = month.lower()
# str1 = 'abc'
# str2 = 'aabccd'

# if month.isalpha():
#
# if month.isdigit():
#
# if month.startswith('abc'):
#
#
# if month.count('a') > 1:
# month = 'Feb'
# day = 12
# print(f'{month:<15}{day}')
# month = 'August'
# print(f'{month:<15}{day}')

# reverse integer
# number = 123456
# new_number = 0
#
# while number > 0:
#     last_digit = number % 10
#     new_number = new_number * 10 + last_digit
#     number = number // 10
#
# print(new_number)

# number = 1230
# str_number = str(number)
# reversed = ''
#
# for digit in str_number:
#     reversed = digit + reversed
#
# print(type(reversed))
# print(int(reversed))

max_value = float('-inf')
second_max_value = float('-inf')

for _ in range(10):
    value = int(input('Enter a value:'))
    if value > max_value:
        second_max_value = max_value
        max_value = value
    elif second_max_value < value < max_value:
        second_max_value = value

print(max_value)

max_value = float('-inf')
min_value = float('inf')

for _ in range(10):
    value = int(input('Enter a value:'))
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value

print(max_value)