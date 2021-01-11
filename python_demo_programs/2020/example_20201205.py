# format
# 1. create a new list
# 2. loop through the original list
# 3. put value into new list basing on conditions

# square numbers
# normal
squares = []
for x in range(10):
    squares.append(x**2)
# comprehension
[x ** 2 for x in range(10)]
[x**2 for x in range(10)]

# get a list with only even numbers
numbers = [1, 2, 3, 4, 5, 6]
# normal
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
# comprehension
print([nifi for n in numbers if n % 2 == 0])

# get a list with only positive numbers
numbers = [1, 2, -3, -4, 5, 6]
# normal
positive = []
for n in numbers:
    if n > 2:
        positive.append(n)
# comprehension
[n for n in numbers if n > 0]

seq = [1, 2, 3, 4]
seq_new = []
for x in seq:
    seq_new.append((x, x**2, x**3))

x = 5
y = x + 3
x = x - 1
z = 10
x = x + z
print(x, y, z)

print(list(range(2, 12, 3)))

