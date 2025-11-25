# numbers = [2, 1, 1, 2, 4, 5]
#
data = {'Alice': [2, 3], 'Tom': 10}
data['bob'] = 100
print(data)
print(data['bob'])

text = 'abbbacdef'
count = {}

for letter in text:
    if letter not in count:
        count[letter] = 1
    else:
        count[letter] = count[letter] + 1

print(len(count.items()))


s = 'abcab'
print(len(s))
#
# max_value = 0
# max_key = ''
# for key, value in count.items():
#     if value > max_value:
#         max_value = value
#         max_key = key
#
# print(max_key)

d = {
    'a': [1, 2, 3]
}

max = -1

for value in d['a']:
    if value > max:
        max = value

print(max)

'''
2025 J3
'''