'''
dictionary/map review
'''
# d = {}
# d['first_name'] = 'Tom'
# d['last_name'] = 'Smith'
#
# print(d)
# print(d['first_name'])


l = [1, 2, 1, 4, 2, 5, 1]

d = {}

for num in l:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

print(d)