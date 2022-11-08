# display_width = 800
# snake_block = 10
#
# index = 20
#
# while index > 0:
#     r = random.randrange(0, display_width - snake_block)
#     print(r)
#     print(round(r))
#     print(round(r / 10.0) * 10.0)
#     print("-------------")
#     index -= 1


# def test(a: int, b: int) -> int:
#     print(a, b)
#     # print(a + b)


# test(1, 2)
# test('abc', 1)
# test('abc', 'bcd')

# def test(a, b):
#     print(a, b)


# a = test

'''
functional programming
- java8 - 2012

object oriented programming

programming paradigm

'''



# for num in input:
#     output.append(negative(num))

# print(output)

# # comprehension
# output = [negative(num) for num in input]

# functional programming: map function

# input = [1, 2, 3, 4]
#
# def negative(n):
#     return -n
#
#
# output = map(negative, input)
# print(list(output))

# languages = ['python', 'perl', 'java', 'c']
# output = [len(s) for s in languages]
# output = list(map(len, languages))

# lambda expression/function


# another common pattern
output = []
input = [1, 2, 3, 4]

def is_even(n):
    return n % 2 == 0


for num in input:
    if is_even(num):
        output.append(num)

print(output)

# write as comprehension
output = [num for num in input if is_even(num)]

output = list(filter(is_even, input))
print(output)

'''
map(fn, iterable)
filter(pred, iterable)
'''

# more examples
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True


# map(float, ['1.0', '3.3', '-2.1'])
# filter(is_prime, range(100))

'''
convert the LHS to the RHS using map/filter

[[1, 3], [4, 2, -5]] -> [4, 1]
[1, True, [2, 3]]    -> ['1', 'True', '[2, 3]']
[0, 1, 0, 6, 'A', 1, 0, 7] -> [1, 6, 1, 7]
'''

'''
list comprehension vs map/filter

memory: 
list comprehension buffers all computed results
map/filter only compute output elemetns when asked

speed:
map/filter faster in some cases

lambda functions/expression
- define anonymous/unnamed function on-the-fly

lambda params: expr(params)
'''

# creates a function object and immediately call it
print((lambda val: val*val)(2))

# use lambda
map(lambda val: val*val, [1, 2, 3, 4])

# without using lambda
def power(val):
    return val*val


map(power, [1, 2, 3, 4])
print(list(filter(lambda pair: pair[1] > pair[0], [[4, 1], [3, 4], [8, 0]])))
