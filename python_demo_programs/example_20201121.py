# loop by keys
d = {"one": 1, "two": 2, "three": 3}
keys = list(d.keys())
print(type(keys))
print(keys)

values = list(d.values())
print(type(values))
print(values)

pairs = list(d.items())
print(type(pairs))
print(pairs)

# loop a list of tuples
for i, j in d.items():
    print(i, j)

# build a histogram from string
# 'aabbc'
# {'a':2, 'b':2, 'c':1}

# Below are the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty', 'Hello']
# values = [10, 20, 30, 'Hi']
# expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Hello': 'Hi'}
