l = [1, 1, 1]

l.append(1)
l.append(2)
l.append(3)
l.append('abc')
l.append(True)
del(l[0])

print(l)

for value in l:
    print(value)

l = [0] * 10
print(l)