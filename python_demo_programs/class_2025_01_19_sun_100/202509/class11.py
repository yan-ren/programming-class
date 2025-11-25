N = int(input())

count = [0, 0, 0, 0, 0]

for _ in range(N):
    line = input()

    # loop through each character in line, check for Y and .
    index = 0
    while index < len(line):
        if line[index] == 'Y':
            count[index] += 1

        index += 1

largest = max(count)

# find position of largest number from the count
position = []
for i in range(len(count)):
    if count[i] == largest:
        position.append(i+1)

print(','.join(map(str, position)))

# index:   0, 1, 2, 3, 4
numbers = [1, 2, 3, 4, 4, 4, 4, 4, 5]

for num in numbers:
    print(num)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

for i in range(len(numbers)):
    print(numbers[i])

numbers[len(numbers) - 1] = numbers[len(numbers) - 1] * 10

'''
exercise:
write a program that create a list like following:
[0, 1, 4, 9, 16, ..., 100]

write a program that find how many negative values in a given list
try to write as many solution as possible
'''
# numbers = []
#
# for i in range(11):
#     numbers.append(i ** 2)

numbers = [1, -2, 3, -4]

for num in numbers:
    if num < 0:
        print(num)

for index in range(len(numbers)):
    if numbers[index] > 0:
        print(numbers[index])

index = 0
while index < len(numbers):
    if numbers[index] > 0:
        print(numbers[index])
    index += 1
