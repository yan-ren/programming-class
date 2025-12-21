'''
Given an integer n, generate all binary strings of length n.

A binary string consists only of characters '0' and '1'.

n = 2

output:

["00", "01", "10", "11"]

n = 0
['']

n = 1
['0', '1']

n = 2
['00', '10', '01', '11']

n = 3
['000, '101', '010', '110', '001', '101', '011', '111']
'''
n = 3
start = ['']
result = []

while start:
    current = start.pop(0)

    if len(current) == n:
        result.append(current)
        continue

    start.append(current + '0')
    start.append(current + '1')

print(result)

