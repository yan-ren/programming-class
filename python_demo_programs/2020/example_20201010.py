# exercise
# write a function that takes a dictionary, return the sum of keys and sum of values

set2 = {'a', 'b', 'c'}
set2.add('a')

print(set2)

for n in set2:
    print(n)

# set1 = set([1, 2, 3, 4])
# set1 = set ('123456')

# find if one string contains the same letter as anther string
# 'abbbcd' 'acbddd'
def diff(str1, str2):
    set1 = set(str1) # {'a', 'b', 'c', 'd'}
    set2 = set(str2) # {'a', 'c', 'b', 'd'}

    if set1 - set2 == {}:
        return True
    else:
        return False


diff('abbbcd', 'acbddd')


set1 = {1, 2, 3, 4}
set2 = {2, 5}
print(set1 - set2)

int()