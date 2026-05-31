'''
For loop

previously we learned while loop
today we are learning another type of loop, which is for loop

most of the time, for loop and while loop can do the same thing, but in cases, use one or the other is simpler
for loop: always used together with other things
while loop: universal
'''
# count from 1 to 10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# for i in range(1, 11):
#     print(i)

# range() gives you a sequence of number
# for i in range(10):
#     print(i)
#
# for i in range(1, 10):
#     print(i)
#
# for i in range(1, 10, 2):
#     print(i)

numbers = [1, 2, 1, 4, 5]

# use while loop to loop through each number
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

# same result using for loop
for num in numbers:
    print(num)

# given a list of numbers, how to calculate the sum using for loop
sum = 0
for num in numbers:
    sum += num

print(sum)

# given a list of numbers, find the largest
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(largest)