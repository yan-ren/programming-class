# dic = {1: 1, 2: 2, 3: 3}
#
# for key in dic.keys():
#     print(key)
#
# for value in dic.values():
#     print(value)
#
# for key, value in dic.items():
#     print(key, value)
#
# dic = {'a': 20, 'b': 30, 'c': 19}
# new_dic = {key:val for key, val in dic if val <= 10}
# new_dic = {key.upper():val for key, val in dic.items()}

print(id(1))
x = 1
y = 2
print(locals())

# homework
# give a dictionary {1: "one", 2:"two", 3:"three"}
# generate a new dictionary with key and tuple, tuple includes the (key, value)
# {1: (1, "one"), 2: (2, "two), 3: (3, "three")}