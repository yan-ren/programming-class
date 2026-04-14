def calculation(a, b):
    return a + b, a - b


c, d = calculation(5, 6)
print(c)
print(d)


def sum_list(nums):
    sum = 0
    for num in nums:
        sum += num

    return sum


numbers = [1, 2, 3, 4]
s = sum_list(numbers)
print(s)

numbers = [4, 2, 5, 6]
print(sum_list(numbers))

# exercise: write a function that takes a list of number as input, find the min/max
def min_max(numbers):
    min = numbers[0]
    max = numbers[0]

    for num in numbers:
        if num > max:
            max = num
        if num < min:
            min = num

    return min, max

# exercise: write a function that takes a list of number as input, find the number of positive vs negative
def positive_negative(numbers):
    count_positive = 0
    count_negative = 0

    for num in numbers:
        if num > 0:
            count_positive += 1
        else:
            count_negative += 1

    return count_positive, count_negative

# print(positive_negative([2, 1, 4]))

# given a list of numbers, find which number is prime number
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print(is_prime(4))
print(is_prime(13))

def find_prime(numbers):
    result = []
    for num in numbers:
        if is_prime(num):
            result.append(num)

    return result

# given a list of numbers, return only the positive value
# numbers = [4, 2, 5, 6]
#
# def add(a, b):
#     global numbers
#     print(numbers)
#     numbers[0] = a + b
#     print(numbers)
#
# add(1, 2)
# print(numbers)

# a = 1
# def foo(a):
#     a = a + 1
#     return a
#
# b = foo(a)
# print(a)
# print(b)

a = [1]
def foo(a):
    a[0] += 1
    print(a)

print(a)
foo(a)
print(a)