result = True

print(result)
print(not result)
result = not result
print(result)

a = True
b = False
print(a and b)

# b and not a or b
# b and not (a or b)
# b and (not a or b)

x = 0
x != 0 and (5/x < 1)

'''
two common ways to change program running order
1. conditional
2. looping
'''
x = int(input('enter a number to check positive'))
# scope ~ range
if x > 0:
    print('x is positive')

    print('done')

'''
in java, use brackets
if (x > 0) {
    System.out.println('');
}
'''