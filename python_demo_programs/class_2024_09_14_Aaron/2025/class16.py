'''
2017 J2
'''
# N = int(input())
# k = int(input())
#
# result = N
#
# for _ in range(k):
#     N = N * 10
#     result += N
#
# print(result)

'''
2016 J2
'''
line1 = input().split(' ')
line2 = input().split(' ')
line3 = input().split(' ')
line4 = input().split(' ')

for i in range(len(line1)):
    line1[i] = int(line1[i])
    line2[i] = int(line2[i])
    line3[i] = int(line3[i])
    line4[i] = int(line4[i])

num1 = sum(line1)
num2 = sum(line2)
num3 = sum(line3)
num4 = sum(line4)
num5 = line1[0] + line2[0] + line3[0] + line4[0]
num6 = line1[1] + line2[1] + line3[1] + line4[1]
num7 = line1[2] + line2[2] + line3[2] + line4[2]
num8 = line1[3] + line2[3] + line3[3] + line4[3]

if num1 == num2 == num3 == num4 == num5 == num6 == num7 == num8:
    print('magic')
else:
    print('not magic')

'''
2015 J2
'''
line = 'How are you :-) doing :-( today :-)?'
count_happy = 0
count_sad = 0

count = 0
for l in line:
    if l == 'a':
        count += 1
