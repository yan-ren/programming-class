empty_set = set()
print(type(empty_set))

a = set('test')
b = set('exam')
print(a & b)

# how do we know if a list has duplicate values using set
# covert the list ot a set and compare the length of set and list
l = [1, 2, 3, 1]
s = set(l)
if len(l) == len(s):
    pass
