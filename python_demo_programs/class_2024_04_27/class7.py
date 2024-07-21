'''
More examples about list
'''
'''
Review in class 6: list
- append
- insert
- del
- remove
- index
- for
- in
'''
# check if a number in the list
# list = [1, 2, 3, 5, 6]
# num = 4
#
# if num in list:
#     print('found')
# else:
#     print('not found')

# alternative
# for value in list:
#     if value == num:
#         print('found')

# remove
list = [1, 1, 2, 3, 4, 5]
list.remove(1)
print(list)

# remove all values
list.clear()

# list concatenation
l1 = [1, 2]
l2 = [2, 3]
l3 = l1 + l2
print(l3)

# example1: given a list of numbers, find the largest
numbers = [1, 2, 3, 1, 5, 2]
# numbers.sort()
# hint: looping
# if len(numbers) == 0:
#     exit(0)

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)

# exercise: how to find out the second largest value from a list

# example2: given a list of number and a target number
# find how many times target number is in the list
numbers = [1, 2, 1, 1, 4, 5, 4]
target = 4
# answer = 2

count = 0
for num in numbers:
    if num == target:
        count += 1

# example3: given two lists with numbers, find the common values in both lists
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

for num1 in l1:
    if num1 in l2:
        print(num1)

for num1 in l1:
    for num2 in l2:
        if num1 == num2:
            print(num1)


# https://github.com/loucadufault/420-LCU-05/blob/master/Assignment-1/A-1_instructions.pdf
print('Please think of a number between 1 and 100')
low = 1
high = 100

while True:
    guess = (low + high) // 2     # keeps the integer part
    print('Is your secret number', guess)
    answer = input('Enter h if my guess is too high, l if too low, or c if I am correct: ')
    if answer == 'h':
        high = guess
    # continue to finish this exercise


# try A1, exercise 2