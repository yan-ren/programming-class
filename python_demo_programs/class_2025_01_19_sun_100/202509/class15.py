
# +++===!!!!
# 777777......TTTTTTTTTTTT
# def process(context):
#     ch = None
#     count = 0
#     result = []
#     for letter in context:
#         if letter != ch and ch != None:
#             result.append(str(count))
#             result.append(ch)
#             ch = letter
#             count = 1
#         elif ch == None:
#             ch = letter
#             count = 1
#         else:
#             count += 1
#
#     result.append(str(count))
#     result.append(ch)
#     return ' '.join(result)
#
# N = int(input())
#
# for _ in range(N):
#     print(process(input()))

s = 'abcde'
l = ['a', 'b', 'c', 'd', 'e']

# print(s[0])
# print(l[0])
#
# for i in s:
#     print(i)
#
# for i in l:
#     print(i)

# print(list(s))
# print(','.join(l))

s = 'a b c d e'
print(s.split(' '))

s = 'a,b,c,d,e'
print(s.split(','))