'''
string
if statement
loop:
- for loop
- while loop

def

list
map - dictionary

set (optional)

class

'''

N = int(input())
x_min = 101
x_max = -1
y_min = 101
y_max = -1
for _ in range(N):
    line = input().split(',')
    # print(line)
    if int(line[0]) < x_min:
        x_min = int(line[0])
    elif int(line[0]) > x_max:
        x_max = int(line[0])
    if int(line[1]) < y_min:
        y_min = int(line[1])
    elif int(line[1]) > y_max:
        y_max = int(line[1])

print(x_min - 1, y_min - 1, sep=',')
print(x_max + 1, y_max + 1, sep=',')