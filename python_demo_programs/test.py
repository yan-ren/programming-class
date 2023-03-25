# n=5
# count=1
# res=[]
# res.append(0)
# for i in range(n//2):
#     res.extend([count,-count])
#     count+=1
# if n%2==0:
#     print(res[1:])
# else:
#     print(res)
#
#
# n = 7
# values = []
# for i in range(1, n // 2 + 1):
#     values.append(i)
#     values.insert(0, -i)
# if n % 2 != 0:
#     values.append(0)
#
# print(values)
#
# def sumZero(n):
#     e = [-x for x in range(1, n)]
#     e.append(sum(abs(x) for x in e))
#     return e
#
# print(sumZero(5))

text = "aabcdaaa"
print(text.count("a"))

from collections import Counter

c = Counter(text)
print(c)
print(c["a"])
