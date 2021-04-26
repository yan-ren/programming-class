# s = 'abcdefgh'
# print(s[0:2])
# print(s[:2]) # implicitly start at 0
# print(s[3:]) # implicitly end at the end
#
# # slice from index 4 to the end
# print(s[4:])

# to achieve the conditional, need to use if keyword
# a = 6
# b = 5
# if b > a:
#     print('inside if statement')
#     print('b is bigger than a')

# # exit the if
# print('program finish')
# a = a + 1

# input = -9
# if input > 0:
#     print('positive')
# else:
#     print('not positive')

# a = 2
# b = 3
# using if, else statement, print the bigger number
# if a > b:
#     print(a)
# else:
#     print(b)

# a = 3
# b = 2
# # given two variables, print the positive variables
# if a > 0
#     print(a)
#
# if b > 0:
#     print(b)

# given a variable, print the variable if it is the even number
# hint: use % operator to find the even or odd
# a = 3
# if a % 2 == 0:
#     print("a is an even number")
# else:
#     print("a is an odd number")

# number = 0
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("zero")

# because input() takes all value as string, need convert to int
# by using int()
# a = int(input("enter the value for a:"))
# b = int(input("enter the value for b:"))
#
# if a > b:
#     print("a is bigger")
# elif a < b:
#     print("b is bigger")
# else:
#     print("a is equal to b")

a = int(input("enter a value for a: "))
if a > 0:
    print("a is positive")
    if a % 2 == 0:
        print("a is even")
    else:
        print("a is odd")
else:
    print("a is negative")