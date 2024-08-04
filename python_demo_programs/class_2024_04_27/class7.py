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
    elif answer == 'l':
        low = guess
    else:
        print('Game Over, your secret number was:', guess)
        break

# try A1, exercise 2
# exercise 2
A_DAYTIME_FREE = 100
A_DAYTIME_COST = 15
A_EVENING = 20
A_WEEKEND = 25

B_DAYTIME_FREE = 200
B_DAYTIME_COST = 20
B_EVENING = 25
B_WEEKEND = 30

C_DAYTIME_FREE = 250
C_DAYTIME_COST = 30
C_EVENING = 35
C_WEEKEND = 40

daytime = int(input('Number of daytime minutes?'))
evening = int(input('Number of evening minutes?'))
weekend = int(input('Number of weekend minutes?'))

plan_a = (daytime - A_DAYTIME_FREE) * A_DAYTIME_COST + A_EVENING * evening + A_WEEKEND * weekend
plan_b = (daytime - B_DAYTIME_FREE) * B_DAYTIME_COST + B_EVENING * evening + B_WEEKEND * weekend
plan_c = (daytime - C_DAYTIME_FREE) * C_DAYTIME_COST + C_EVENING * evening + C_WEEKEND * weekend

if plan_a <= plan_b and plan_a <= plan_c:
    print('Choose Plan A')
elif plan_b <= plan_a and plan_b <= plan_c:
    print('Choose Plan B')
else:
    print('Choose Plan C')

list = [plan_a, plan_b, plan_c]
min_plan = min(list)
if min_plan == plan_a:
    print('Choose Plan A')
elif min_plan == plan_b:
    print('Choose Plan B')
else:
    print('Choose Plan C')

# assignment 2: https://github.com/loucadufault/420-LCU-05/blob/master/Assignment-2/A-2_instructions.pdf
