#
# Y = int(input())
# Y += 1
#
# def is_distinct(number):
#     number = str(number)
#     for digit in number:
#         if number.count(digit) > 1:
#             return False
#
#     return True
#
# while True:
#     if is_distinct(Y):
#         print(Y)
#         break
#     Y += 1
#
#
'''
*x*
 xx
* *

***xxx***
***xxx***
***xxx***
   xxxxxx
   xxxxxx
   xxxxxx
***   ***
***   ***
***   ***
'''
line1 = '*x*'
line2 = ' xx'
line3 = '* *'

k = int(input())
new_line1 = ''
for ch in line1:
    new_line1 = new_line1 + ch * k

for i in range(k):
    print(new_line1)


