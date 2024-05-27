# money = int(input('enter the money:'))

# # this program has logic error, the condition is in the wrong order
# if money > 0:
#     print('positive amount')
# elif money > 1000:
#     print('a large amount')
# else:
#     print('not sufficient amount')

# # fix
# if money > 1000:
#     print('a large amount')
# elif money > 0:
#     print('positive amount')
# else:
#     print('not sufficient amount')



salary = int(input('Enter your salary:'))
years = int(input('Enter years of service:'))

# complete the program
if years > 5:
    bonus = salary * 0.05
    print('your bonus is', bonus)
else:
    print('no bonus')


number1 = int(input('Enter the first number:'))
number2 = int(input('Enter the second number:'))

if number1 > number2:
    print('First number is the largest')
elif number2 > number1:
    print('Second number is the largest')
else:
    print('The first number and second number is the same')

'''
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity. Suppose, one unit will cost 100.
Judge and print total cost for user.
'''
quantity = int(input('How many item do you want to buy?'))
price = quantity * 100

if quantity > 1000:
    print(price * (1-0.1))
else:
    print(price)

'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''
marks = int(input('Enter your grade:'))
if marks > 80:
    print('You get grade A')
elif 60 < marks <= 80:
    print('You get grade B')
elif 50 < marks <= 60:
    print('You get grade C')
elif 45 < marks <= 50:
    print('You get grade D')
elif 25 < marks <= 45:
    print('You get grade E')
else:
    print('You get grade F')