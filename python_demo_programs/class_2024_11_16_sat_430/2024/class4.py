'''
while
for
'''

# i = 0
# while i < 10:

s = 'abcdef' # iterable item
num = 123455

for c in s:
    print(c)

# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

# for i in range(10):
#     print(i)
#
# # i = 0
# # while i < 10:
# #     i += 1
#

'''
Count vowels in a sentence

write a program:
1. take a sentences as input from user
2. Count then number of a e i o u in the sentence
3. print the count of vowels
'''

# s = 'abcdef'
# for ch in s:
#     ch = 'a'
#
# print(s)

for row in range(5):
    for col in range(5):
        print('#', end='')
    print()

'''
#
##
###
####
'''
'''
1  2  3  4  5  
2  4  6  8  10  
3  6  9  12  15  
4  8  12  16  20  
5  10  15  20  25  
'''
'''homework
    *    
   ***   
  *****  
 ******* 

'''

'''
() - tuple, function
[] - list, index
{} - dictionary
'''
l = [3, 2, 3, 'abc']
print(len(l))
print(len(l[3]))

for value in l:
    print(value)

'''
Given a list of number, find the max and min
e.g. [1, 2, 1, 5, 2, 4]

'''
numbers = [-1, -2, -1, -5, -2, -4]

min = numbers[0]
max = numbers[0]

for num in numbers:
    if num > max:
        max = num
    if num < min:
        min = num

print(max, min)

'''
Given a list of numbers, calculate the average
e.g.
[1, 2, 1, 2, 10, 12]

result = 1.5
'''
numbers = [1, 2, 1, 2, 10, 12]
sum = 0

for num in numbers:
    sum += num

print(sum / len(numbers))
