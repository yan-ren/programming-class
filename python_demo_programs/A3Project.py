# A3 Advanced Loops Assignment
# Starter code by David Johnson and Miriah Meyer
# For COMP1010 University of Utah
#
# Assignment written by

# The print function outputs text and adds a new line at the end to go to the next line.
# Sometimes, we would like the output of two different prints to end on the same line.
# Compare
print("Good")
print("Day")
# with
print("Good", end=' ')
print("Day")
# The end= addition tells print to end its output with whatever is assigned to end. In this case, it
# is a blank space instead of the usual new line.
#
# Note that we have to be careful of spacing by adding in a blank space ourselves with the end=' '.
# If no space is wanted, you can use end='', in which case nothing is added to the end of the print.
#
# This new form of print is useful in a loop. A print in a loop body can add more information
# to a single line and not take as much space.
# A common pattern is to use print with a end=' ' in the loop body, and then add a
# print() after the loop to go to a new line.
# If I wanted to print numbers from 1 to 5 all on one line, the code could look like
for value in range(1,6):
    print(value, end=' ')
print()

# 1) Using a for loop, print out numbers from -5 to 0 (including -5 and 0).
# Your result should look like
# -5
# -4
# -3
# -2
# -1
# 0

for i in range(-5, 1):
    print(i)


# 2) Using a for loop, print out numbers in steps of 5 from 0 to 25 (including 0 and 25) all on one line.
# Your result should look like
# 0 5 10 15 20 25
for i in range(0, 26, 5):
    print(i, end=' ')

print()
# 3) Using a for loop, print out every other character in a name variable with a space between each letter.
# With the name 'Whitaker', the output would be
# W i a e
s = 'Whitaker'
for i in range(0, len(s), 2):
    print(s[i], end = ' ')

# 4) Using a single accumulator loop, a) compute and print the result of adding even numbers from 0 to 10, and b) concatenate and print the numbers into a string with a space between each number.
# Your output would be
# 30
# 0 2 4 6 8 10

result = 0
for i in range(0, 11, 2):
    result = result + i

print(result)

s = ''
for i in range(0, 11, 2):
    s = s + str(i) + ' '

print(s)

# 5) Use the input function to ask for a dollar amount of a restaurant bill. Assume the entered dollar amount is a
# float (a number with a decimal part).
# Print out a 20% tip (multiply the given number by 0.2) along with a helpful message. As an example, if the
# user entered 10.40 for the bill amount, the tip should be 2.08
# Do not worry about making the tip amount have 2 decimal places like a dollar amount would.
amount = float(input('enter a number'))
print('user entered', amount, 'for the bill amount', 'the tip should be', amount * 0.2)

# 6) Use the input function to ask for a dollar loan amount (assume a float is entered).
# Then ask for a loan rate percentage amount (Assume a float is entered).
# Then ask for the number of years (assume a positive int is entered).
# Make sure there are helpful messages saying what should be entered.
# Print out a chart showing how the loan would grow each year if no money is used to pay it off. As an example
#
# Please enter a loan amount: 1000.0
# Please enter a loan rate percent: 5.0
# Please enter the length of the loan in years: 5
# Year: 1 Loan Amount: 1050.0
# Year: 2 Loan Amount: 1102.5
# Year: 3 Loan Amount: 1157.625
# Year: 4 Loan Amount: 1215.5062500000001
# Year: 5 Loan Amount: 1276.2815625000003
#
# The math to compute this is not too bad.  Each year, the updated loan value is:
#   loan amount * (1 + loan rate percent/100.0)
# If the person entered 5.5 for the loan rate, the math evaluates to
# new loan amount = old loan amount * 1.055.
# Use a for loop over the number of years and compute an updated loan amount each year and print it out.


loan = float(input('Please enter a loan amount:'))
rate = float(input('Please enter a loan rate percent:'))
years = int(input('Please enter the length of the loan in years:'))

for i in range(5):
    loan = loan * (1 + rate/100.0)
    print('Year:', i, 'Loan Amount:', loan)

# 7) Use the turtle module and the example slide of code from lecture 7 to make a grid of circles.
# Modify the code so that instead of making a square grid, it makes a triangle shaped grid. See the assignment page for
# an example result. This can be done with only a small change to the nested loops - find that small change way
# to solve this.
for r in range(1, 6):
    for c in range(r):
        print('*', end='')
    print()
