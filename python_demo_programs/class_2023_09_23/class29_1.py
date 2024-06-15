s = set()
s.add(1)
s.add(2)

print(s)
s.add(1)
print(s)

l = [1, 2, 1, 3, 2, 4]
l = list(set(l))
print(l)

if 2 in s:
    print('')
    
s1 = set()
s1.add(1)
s1.add(2)

s2 = set()
s2.add(2)
s2.add(3)

s3 = s1 | s2 # combine value in set1 and set2 by removing duplicate
print(s3)

s3 = s1 & s2 # value both in set1 and set2
print(s3)

s3 = s1 - s2 # value in set1 but not in set2
print(s3)
s3 = s2 - s1 # value in set2 but not in set1
print(s3)