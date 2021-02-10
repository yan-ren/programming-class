# list = [0, 1, 2, 3]
# [1, 3, 5, 7]
# [i*2+1 for i in list]

list = [3, 8, 9, 5]
# res = []
# for i in list:
#     if i % 3 == 0:
#         res.append(True)
#     else:
#         res.append(False)
res = [True if i % 3 == 0 else False for i in list]

list = ['apple', 'orange', 'pear']
res = []
for i in list:
    res.append(i[0].upper())

res = [i[0].upper() for i in list]

[(i, len(i)) for i in list]