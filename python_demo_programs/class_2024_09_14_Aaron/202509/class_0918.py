'''
dictionary
'''

# counts = {'apple': 1}
# counts['banana'] = 2
# print(counts)
# del counts['banana']
# print(counts)

# Count how many times each word appears in a list
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)


a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

# {'x': 1, 'y': 5, 'z': 4}
merged = {}

for key, value in a.items():
    merged[key] = value

for key, value in b.items():
    if key in merged:
        merged[key] = merged[key] + value
    else:
        merged[key] = value

print(merged)


grades = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [70, 65, 72],
    "Diana": [88, 79, 85]
}

# Write a program to calculate the average score for each student and store it in a new dictionary.
# Example output:
# {'Alice': 84.33, 'Bob': 91.67, 'Charlie': 69.0, 'Diana': 84.0}
