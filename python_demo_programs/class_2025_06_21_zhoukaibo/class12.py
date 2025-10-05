# def welcome():
#     print('hello')
#     print('welcome to the class')

def calculation(a, b):
    result = (a + b) / (a * b)
    return result

r = calculation(2, 3)
print(r)

def welcome(name):
    print('Hello', name)

# welcome()
# welcome()
# calculation(1, 2)
# welcome('Alice')
# welcome('Bob')


# write a function called compare, takes two number as input, print the larger number
def compare(num1, num2):
    if num1 > num2:
        print(num1)
    elif num2 > num1:
        print(num2)
    else:
        print('same')


compare(1, 2)
compare(2, 3)

numbers = [1, 2, 3, -1, -3]

# write a function that takes a list of number as input, return the sum of all numbers

# write a function that takes a list of number as input, return a new list with only positive numbers
# new_numbers = []
# for num in numbers:
#     if num > 0:
#         new_numbers.append(num)
# print(new_numbers)

def find_positive(numbers):
    new_numbers = []
    for num in numbers:
        if num > 0:
            new_numbers.append(num)
    return new_numbers

# write a function that takes two lists as input, and merge them return a single list
def merge(l1, l2):
    result = []
    for value in l1:
        result.append(value)
    for value in l2:
        result.append(value)

    return result

print(merge([1, 2, 3], [2, 4]))