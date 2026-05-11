'''
read the code and figure out what's the output
'''
# q1
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a, b)

# q2
# def modify(lst, x):
#     lst = lst + [x]
#     return lst
#
# nums = [1, 2, 3]
# modify(nums, 4)
# print(nums)

# q3
# s = "science"
# result = ""
# for i in range(len(s)):
#     if i % 2 == 0:
#         result += s[i].upper()
#     else:
#         result += s[i]
# print(result)

# q4
# def f(n):
#     if n == 0:
#         return 1
#     return n * f(n - 1)
#
# print(f(4))

# q5
# d = {"a": 1, "b": 2, "c": 3}
# total = 0
# for key in d:
#     total += d[key]
# print(total)
#
# for value in d.values():
#     total += value
#
# for k, v in d.items():
#     total += v

'''
Write a function fizzbuzz(n) that returns a list of strings for numbers 1 to n: "Fizz" if divisible by 3, 
"Buzz" if divisible by 5, "FizzBuzz" if both, otherwise the number itself as a string.
'''
# def fizzbuzz(n):
#
#
# fizzbuzz(20)

'''
Write sum_digits(n) that returns the sum of the digits of a string. Example: sum_digits('12345') → 15.
'''

'''
Write a function multiplication_table(n) that prints an n × n multiplication table, from 1x1 to nxn
'''
def multiplication_table(n):
    for first in range(1, n + 1):
        for second in range(1, first+1):
            print(first, 'x', second, '=', first * second)


multiplication_table(9)