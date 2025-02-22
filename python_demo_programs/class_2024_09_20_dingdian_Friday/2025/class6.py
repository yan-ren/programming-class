# function/method
def welcome():
    print('welcome to the class')
    print('today is a good day')

def calculation(a, b):
    result = (a - b) / (a + b)
    return result 


print(calculation(1, 2))


'''exercise

write a function which takes one value as input, return the sum from 1 to the input value

'''
def f1(n):
    res = 0
    for i in range(1, n + 1):
        res = res + i

    return res

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i

    return res




print(f1(3))
print(f1(5))

numbers = [1, 2, 3, 1, 4]

'''
create a function which takes a list as input, and return the sum of all values from the list

e.g. if you call function with [2, 3, 4, 2], you get 11
'''
def sum_list(l):
    res = 0
    for value in l:
        res = res + value
        
    return res

print(sum_list([1, 2, 3, 1]))


def cal(a, b):
    return a+b, a-b

v1, v2 = cal(1, 2)
print(v1)
print(v2)

'''
Write a function which takes a list of number as input, return the max and min value in the list

e.g.
if given [1, 2, 1, 5, 2]
get 5, 1
'''