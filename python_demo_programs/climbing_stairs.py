'''
fibonacci sequence
The sequence follows the rule that each number is equal to the sum of the preceding two numbers.
The Fibonacci sequence begins with the following 14 integers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233

take n steps to reach the top

base case:
n == 0, 0 way
n == 1, 1 way
n == 2, 2 ways, 1 way is to climb one stair from n == 1,
and another way is to climb 2 stairs from n == 0
'''

# recursive solution
def climb_stair(n):
    # base case
    if n == 0 or n == 1 or n == 2:
        return n

    return climb_stair(n-1) + climb_stair(n-2)


print(climb_stair(3))

# non-recursive solution
def climb_stair(n):
    if n == 1:
        return 1
    a = 1
    b = 2

    while n > 2:
        tmp = b
        b = a + b
        a = tmp
        n -= 1

    return b

print(climb_stair(3))

'''
functional programming

is one of the programming paradigms
object oriented programming

java
- java8 - 2012

python
- 

first class function


functional programming
- design and write your code in terms of function
- the output depends on which function you passed in

why functional programming
- improve productive
- easy debug
- modularity: encourages small independent functions
'''
'''
# a common pattern
input = [1, 2, 3]
output = []

def negative(n):
    return -n


for num in input:
    output.append(negative(num))

print(output)

# comprehension
output = [negative(num) for num in input]

# functional programming
output = list(map(negative, input))
print(output)

# comprehension
languages = ['python', 'perl', 'java', 'c']
output = [len(s) for s in languages]

# functional programming
output = list(map(len, languages))
print(output)
'''

# another common pattern
input = [1, 2, 3, 4, 5]
output = []

def is_even(n):
    return n % 2 == 0


for num in input:
    if is_even(num):
        output.append(num)

print(output)

# comprehension
output = [num for num in input if is_even(num)]

# functional programming
output = list(filter(is_even, input))
print(output)

# summarize
# map(fn, iterable)
# filter(pred, iterable)

# more examples
def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True


print(list(map(float, ['1.0', '3.3', '-4.2'])))
# range(100) -> [0, 100)
print(list(filter(is_prime, range(100))))
