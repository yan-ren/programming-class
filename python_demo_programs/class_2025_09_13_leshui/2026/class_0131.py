D = int(input())

while True:
    Y = int(input())
    if Y < D:
        D += Y
    else:
        break

print(D)