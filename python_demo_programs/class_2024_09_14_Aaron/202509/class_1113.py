'''
String

'''
text = 'abcde'

# use while loop to loop each character in string
# index = 0
# while index < len(text):
#     print(text[index])
#     index += 1

# for loop
# for ch in text:
#     print(ch)

# use while loop to create a reversed string


# given a string, count how many vowels
# s = 'hello'
# vowels = 'aeiou'
#
# numbers = [[1, 2, 3], [2, 4, 1], [2, 4]]

count = [0, 0, 0, 0, 0]

N = int(input())

for _ in range(N):
    line = input()
    i = 0
    while i < len(line):
        if line[i] == 'Y':
            count[i] += 1
        i += 1

largest = max(count)
position = []

i = 0
while i < len(count):
    if count[i] == largest:
        position.append(i + 1)
    i = i + 1


print(','.join(map(str, position)))

'''
sample question: given you a list of numbers and a target, find the first and last position 
of the target in the list
'''
numbers = [2, 3, 1, 4, 3, 3, 5]
target = 3
first = -1
last = -1

index = 0
while index < len(numbers):
    if numbers[index] == target:
        if first == -1:
            first = index
        last = index

print(first, last)