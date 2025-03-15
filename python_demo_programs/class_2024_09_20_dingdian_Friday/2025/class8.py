'''
exercise: write a function which takes an integer called n
as input
and return a list with numbers from 1 to n
[1, 2, 3, ..., n]
'''
def generate(n):
    res = []

    for i in range(1, n+1):
        res.append(i)

    return res


'''
exercise:
write a function which takes one list of numbers,
return the number of positive value and number of negative value

input: [1, 2, -1, 2, -3]
return 3, 2
'''
def count_positive_negative(numbers):
    positive = 0
    negative = 0

    for num in numbers:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1

    return positive, negative