'''
python basic data structure:
- list
- tuple
- dictionary
- set
'''

numbers = [1, 2, 1, 2, 4, 5]
d = {'Tom': 23, 'Jerry': 20, 'Bob': 19}

print(d['Tom'])
print(d['Jerry'])
print(d['Bob'])

d['Bob'] = 20

# loop by key
for k in d.keys():
    print(k, d[k])

# loop by value
for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

d['Cherry'] = 21
del d['Cherry']


print(d)
print(len(d))

'''
given a string, find the most frequent letter

s = 'abcdeeeabc'

'''
count = {}
s = 'abcdeeeabc'

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)

most_frequent = 0
most_frequent_letter = ''

for k, v in count.items():
    if v > most_frequent:
        most_frequent = v
        most_frequent_letter = k

print(most_frequent_letter)

d = {'Tom': [20, 30, 50], 'Alice': [20, 23, 40], 'Bob': [50, 60, 40]}

for name, grades in d.items():
    avg = sum(grades) / len(grades)
    print(name, 'avg:', avg)

d = {'Tom': {'English': 90, 'Math': 88, 'Physics': 77}, 'Jerry': {'English': 90, 'Math': 68}}

for name, grades in d.items():
    # grades?
    avg = sum(list(grades.values())) / len(grades)
    print(name, 'avg:', avg)

# d = {[20, 30, 50]: 'Tom'}
words = ["cat", "dog", "elephant", "bird", "ant", "lion", "hippo", "ox"]
'''
{
    3: ["cat", "dog", "ant"],
    8: ["elephant"],
    4: ["bird", "lion"],
    5: ["hippo"],
    2: ["ox"]
}
'''
d = {}
for word in words:
    if len(word) in d:
        d[len(word)].append(word)
    else:
        d[len(word)] = [word]

print(d)

'''
given two words, how to determine they are made with same letters
word1 = 'eat'
word2 = 'ate'

word1 = 'cat'
word2 = 'act'

word1 = 'abca'
word2 = 'aabc'
'''