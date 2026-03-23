
found_subsets = [1, 2, 3]
print(found_subsets)
print(*found_subsets)

candidates = [1, 2, 3, 4, 5]
min_hops = 4
tmp = [x for x in candidates if x>min_hops]
print(type(tmp))
second_min=min(tmp)
print(second_min)