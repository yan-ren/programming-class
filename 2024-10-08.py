a = 10
s = 'abcd'

# data structure
l = []
l.append(2)
l.append(10)

print(l[1])
print(l)

'''
string has indexing, but string immutable
'''

s = 'abcd'
print(s[0])
# s[0] = 'A'

# reassign is allowed
s = 'efd'

l = ['abd', 'efd', 'abe'] # mutable
l[0] = 'abc'

matrix = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]

print(matrix[0][1])
for row in matrix:
    for col in row:
        print(col)

row = 0
while row < len(matrix):
    col = 0
    while col < len(matrix[row]):
        print(matrix[row][col])
        col += 1
    row += 1

# range(4) -> [0, 1, 2, 3]
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col])


def symmetric(m):
    # check if the number of rows equals the number of columns
    rows = len(m)
    for row in m:
        if len(row) != rows:
            return False

    # check if the element in row i and column j equal to the element in row i and column i
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != m[j][i]:
                return False

    return True

matrix1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matrix2 = [
    [0, -1, 11, -8],
    [-1, 4, 5, 12],
    [11, 5, 6, 0],
    [-8, 12, 0, -3]
]

print(symmetric(matrix1))
print(symmetric(matrix2))

# exercise: find the largest value from the list
numbers = [-1, -2, -3, -10]
max = numbers[0]

for value in numbers:
    if value > max:
        max = value

print(max)

# exercise: find the largest value from the matrix
max = matrix1[0][0]
for row in matrix1:
    for value in row:
        if value > max:
            max = value

print(max)

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if matrix1[i][j] > max:
            max = matrix1[i][j]

# loop from left to right using for loop
s = 'abcde'
for char in s:
    print(char)

# loop from left to right using while loop
index = 0
while index < len(s):
    print(s[index])
    index += 1

# loop from right to left using index
index = len(s) - 1
while index >= 0:
    print(s[index])
    index -= 1

s_rev = reversed(s)
# for char in s_rev:
#     print(char)

print(''.join(s_rev))



