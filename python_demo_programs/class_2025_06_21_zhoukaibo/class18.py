D = int(input())

E = int(input())

for _ in range(E):
    sign = input()
    amount = int(input())

    if sign == '+':
        D += amount
    else:
        D -= amount

print(D)