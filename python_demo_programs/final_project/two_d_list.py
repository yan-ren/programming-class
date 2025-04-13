matrix = []

for value in range(4):
    matrix.append([value - 1, value, value + 1])

print(matrix)

s = 0
for row in matrix:
    s += sum(row)

print(s)

s = 0
for row in matrix:
    for value in row:
        s += value

print(s)

def multiply(A, B):
    if len(A[0]) != len(B):
        return

#   A: mxn, b: nxk = mxk
    result = []
    for _ in range(len(A)): # m
        row = []
        for _ in range(len(B[0])): # k
            row.append(0)
        result.append(row)

    for row_index in range(len(A)):
        for col_index in range(len(B[0])):
            total = 0
            for element_index in range(len(B)):
                total += A[row_index][element_index] * B[element_index][col_index]
            result[row_index][col_index] = total

    return result

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print(multiply(A, B))

# Transpose a matrix
A = [[1, 2, 3],
     [4, 5, 6]]
# Output: [[1, 4], [2, 5], [3, 6]]
def transpose(A):
    result = []
    for _ in range(len(A[0])):
        row = []
        for _ in range(len(A)):
            row.append(0)
        result.append(row)

    for col_index in range(len(A[0])):
        for row_index in range(len(A)):
            result[col_index][row_index] = A[row_index][col_index]

    return result

# print(transpose(A))

numbers = [1, 2, 3, 4, 5]
numbers_slice = numbers[::-1]
print(numbers)
print(numbers_slice)
numbers[4] = 50
print(numbers)
print(numbers_slice)

