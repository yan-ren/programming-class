'''
data structure: organize values in a better way
list: linear data structure, values are organized one after another
'''
a = 1
b = 'abc'

# create a list
l = []

# add value at the end of the list
l.append(10)
l.append(20)
print(l)

# returns the numver of elements witht hte specified value
print(l.count(10))

# extend: add the elemts of a list to another list
# l = [10, 20] -> [10, 20, 20, 30, 40]
l.extend([20, 30 , 40])
print(l)

# index: return the index of the first element with the specified value
print(l.index(20))

# insert: insert element at the spcified index
print(l)
l.insert(1, 100)
print(l)

# remove: removes the first item with the specified value
l.remove(20)
print(l)

# sort: arrage the list in increasing order
print(l)
l.sort()
print(l)

# check if a value is in list using if
# if 20 in l:

# loops all values in list
for i in l:
    print(i)


index = 0
while index < len(l):
    print(l[index])
    index += 1


'''
write loops to find out the max and min value in the list, how?
'''
numbers = [1, 2, 3, 1, 4, 50, 20]
# [-2, -3, -4]
largest = numbers[0]
# largest = 0
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print(largest)

'''
given list a numbers, calculate the average of the numbers
e.g.
[1, 2, 1, 3] -> 1.75
'''

sum = 0
for n in numbers:
    sum += n

print(sum / len(numbers))


'''
generate a list with all even numbers below 20
e.g

[0, 2, 4, 6, 8 ... 18]
'''

# i = 0
# result = []
# while i <= 20:
#     result.append(i)
#     i += 2


# i = 0
# while i <= 20:
#     if i % 2 == 0:
#         result.append(i)
#     i += 1

'''
given a list of numbers, return a list with the squre for each value
[2, 1, 2, 4, 5]
[4, 1, 4, 16, 25]
'''
numbers = [2, 1, 2, 4, 5]
index = 0
while index < len(numbers):
    numbers[index] = numbers[index] * numbers[index]
    index += 1


'''
given a list of numbers, print the number of positive numbers and negative numbers

[1, 2, 1, -2, -2]
3
2
'''

'''
priority queue
1. implementation
2. 



given a list of numbers in sorting
[-20, -10, 0, 15, 25]

[0, 10, 15, 20, 25]
'''