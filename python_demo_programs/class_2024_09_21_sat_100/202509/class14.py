T = input()
S = input()

current = S

for _ in range(len(S)):
    if current in T:
        print('yes')
        break

    current = current[1:] + current[0]
else:
    print('no')