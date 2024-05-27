# a = int(input('enter a number:'))

# if a > 0:
#     print('a is positive')
# elif a < 0:
#     print('a is negative')
# else:
#     print('a is zero')


# if a % 2 == 0:
#     print('even number')
# else:
#     print('odd number')

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print('a is the largest')
elif b > a and b > c:
    print('b is the largest')
else:
    print('c is the largest')