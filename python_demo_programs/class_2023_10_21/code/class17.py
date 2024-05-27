d = {}
d['firstname'] = "jack"
d['lastname'] = 'stan'

print(d)
print(d['firstname'])

# del d['firstname']

print(len(d))

# homework: given a string, create a dictionary which counts for each letter how many times it shows in the string
s = 'abccddef'

# d = {}
# for letter in s:
#     if letter in d:
#         d[letter] += 1
#     else:
#         d[letter] = 1
#
# print(d)

# d = {}
# for letter in s:
#     if letter not in d:
#         d[letter] = 1
#     else:
#         print(letter)

# create a dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d = {}
for i in range(1, 7):
    d[i] = i*10

print(d)

# create a dictionary: {10:90, 20:80, 30:70, 40:60, 50:50, 60:40, 70:30, 80:20, 90:10}
