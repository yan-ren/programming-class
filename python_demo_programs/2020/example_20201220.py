dic = {"one":1, "two":2}
s = {1, 2, 3, 4}
s.add(10)
# s = {} # this defines an empty dictionary
# s = set() # this defines an empty set
for i in s:
    print(i)

a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)
print(b - a)
print(a | b)
print(a & b)
print(a ^ b)
a |= b # => a = a | b

# practice
# how to know a string is constructed using unique letter
# "apple", "bear"
s = "apple"
if len(set(s)) == len(s):
    print("all unique characters")
else:
    print("some are removed")

# old question, remove the duplicate values from the list
# [1, 2, 2, 3] -> [1, 2, 3]
# how to solve it using set
l = [1, 2, 2, 3]
l = list(set(l))
print(l)

# old way
new_l = []
for i in l:
    if i not in new_l:
        new_l.append(i)