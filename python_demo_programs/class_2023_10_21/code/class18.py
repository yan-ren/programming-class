# d = {}
d = dict()
d['one'] = 1
d['two'] = 2
d['three'] = 3

# for key in d:
#     print(key, d[key])
#
# d_new = {}
# for key, value in d.items():
#     d_new[value] = key
d1 = {'one': 1, 'two': 2}
d2 = {'one': 1, 'three': 3}
# {'one': 2, 'two': 2, 'three': 3}
merge = {}
for key, value in d1.items():
    merge[key] = value

for key, value in d2.items():
    if key in merge:
        merge[key] = merge[key] + value
    else:
        merge[key] = value

print(merge)