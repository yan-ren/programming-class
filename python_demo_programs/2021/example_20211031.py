
list1 = [1, 4, 5, 6]
list2 = [2, 3]

for i in list2:
    for j in list1:
        if j < i and i not in list1:
            list1.insert(i-1, i)

print(list1)


l = [1, 1, 2, 2, 2, 3, 4, 5]
# delete all 2s from the list
index = 0
while index < len(l):
    if l[index] == 2:
        del l[index]
        index -= 1
    index += 1


index = len(l) - 1
while index >= 0:
    if l[index] == 2:
        del l[index]
    index -= 1



