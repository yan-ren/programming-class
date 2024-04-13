from collections import defaultdict
from collections import ChainMap


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1, d2, d3)
print(c)
print(c.maps)
print(list(c.keys()))

new_dic = {'f': 5}
c = c.new_child(new_dic)
print(c)
print(c['a'])
del c['f']
del d1['a']
print(c)

