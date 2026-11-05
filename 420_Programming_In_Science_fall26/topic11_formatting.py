price = 3.3
count = 8
# text = 'Total cost: ' + str(price * count) + " dollars"
text = f'Total cost: {price * count:.2f} dollars'
print(text)

x = 1010.0000
print(f'{x:15f}') # right aligned

'''
d - format integer
f - format float
e - format exponent
s - format string
'''

text = 'hello'
print(f'{text:15s}') # left aligned

y = 123.4567
print(f'{y:10.2f}') # 10 is the total width, 2 is two decimal points