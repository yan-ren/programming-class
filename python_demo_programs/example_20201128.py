# given two dictionaries with no common keys, combine them into one dictionary
# {1: 1, 2: 2, 3: 4}
# {3: 3}
# return {1: 1, 2: 2, 3: 7}

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print(list(zip(questions, answers)))

l = [1, 0, 29, 3]
print(sorted(l))

squares = []
for x in range(10):
    squares.append(x**2)


squares = [x ** 2 for x in range(10)]

''' Delete set of keys from Python Dictionary
Given:
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keysToRemove = ["name", "salary", ]

Expected output: {'city': 'New york', 'age': 25}
'''
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

print(sampleDict)

