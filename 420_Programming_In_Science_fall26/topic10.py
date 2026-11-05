x = [2, 1, 4, 2, 5]
print(len(x))
print(max(x))
print(min(x))
print(sum(x))

print(sorted(x))
print(x)
print(x.index(5)) # 4
print(x.index(2)) # 0

print(x.count(5))

text = 'hello world'
print(text.upper())
print(text.lower())
print(text.split()) # gives list of values, broken at space
new_text = text.replace('h', 'w')
print(new_text)
print(text.isdigit()) # if only consists digits, True or False
print(text.isalpha()) # if only consists letters, True or False
