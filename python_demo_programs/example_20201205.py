# format
# create a new list
# loop through the original list
# put value into new list basing on conditions

# square numbers
# normal
squares = []
for x in range(10):
    squares.append(x**2)
# comprehension
[x ** 2 for x in range(10)]

# get a list with only even numbers
numbers = [1, 2, 3, 4, 5, 6]
# normal
even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
# comprehension
print([n for n in numbers if n % 2 == 0])

# get a list with only positive numbers
numbers = [1, 2, -3, -4, 5, 6]
# normal
positive = []
for n in numbers:
    if n > 2:
        positive.append(n)
# comprehension
[n for n in numbers if n > 0]
