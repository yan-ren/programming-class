# print(1+1)

# I -> Input
# O -> Output

# name = input('What is your name?')
# print("welcome " + name)

# answer = True
# # answer = False
# print(type(answer))
# print(answer)

# print(6 != 5)
# print(10 > 8)
# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not a)
# print(not b)
'''
character: letter, number and symbol
letter: abcdABCD...
number: 123...
symbol: !@#$%...
'''

# a = "hello "
# b = "world"
# c = a + b
# print(c)

# a = 1
# b = 2
#
# temp = a
# a = b
# b = temp
#
# print(a)
# print(b)

# a = 1
# a = str(a)
# print(type(a))


# def canThreePartsEqualSum(sample):
#     if sum(sample) % 3 != 0:
#         return False
#
#     goal = sum(sample) / 3
#     partition_sum = 0
#     counter = 0
#     # loop and add
#     for i in sample:
#         partition_sum += i
#         if partition_sum == goal:
#             counter += 1
#             partition_sum = 0
#
#     return counter == 3
#
#
# print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
# print(canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
# print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))

'''
character: letter, number, symbol
'''
s = "abc def"
# print(s)
# print(s[0])
# print(s[2])
'''
length of string: number of character
length of string vs largest index
largest index = length of string - 1
'''
# print(len(s))
# print(s[6])
# print(s[-1])
# print(s[2:5])
'''
write a program to check user's input is positive or not
'''
# a = int(input("enter a number:"))
# if a > 0:
#     print("positive")
# elif a < 0:
#     print("negative")
# else:
#     print("zero")
#
# print("end")

a = 1
b = 2
c = 4

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
