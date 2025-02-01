# a = 1
# b = 1.0
# c = True
# d = 'abc'
#
# print(type(a))
# a = 1.0
# print(type(a))
#
# student_name = 'Tom'

a = 1
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b) # float division
print(a // b) # integer division
print(a ** b)
print(a % b)

c = a
a = b
b = c
print(a, b)

# a = int(input('Enter a number:'))

print(a, b, sep='', end='')
print(b, c)

name = 'Tony'
print(f'My name is {name}')
# print('My name is ' + name)

number = int(input("Please enter a whole number: "))
print(f"Data type of inputted value: {number} is {type(number)}.")

number = float(input("Please enter a decimal number: "))
print(f"Data type of inputted value: {number} is {type(number)}.")

_bool = input("Please enter 'true' or 'false': ")
_bool = _bool == "true"  # Convert to boolean
        # True
if _bool == "true":
    _bool = True        # Convert to boolean