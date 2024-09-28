'''
exercise: 2023 J2
'''
'''
count = int(input())
chili = []

for i in range(count):
    chili.append(input())

shu = 0
for c in chili:
    if c == 'Poblano':
        shu += 1500
    elif c == 'Mirasol':
        shu += 6000
    elif c == 'Serrano':
        shu += 15500
    elif c == 'Cayenne':
        shu += 40000
    elif c == 'Thai':
        shu += 75000
    elif c == 'Habanero':
        shu += 125000
        
print(shu)
'''

# text = ['hello', 'world', 'welcome']
# new_text = []
# for s in text:
#     new_text.append(s[1:])
#
# print(new_text)
#
# new_text = [s[1:] for s in text]

numbers = [1, 2, 3, 4]
new_numbers = []

for num in numbers:
    if num % 2 == 0:
        new_numbers.append(num)

#
new_numbers = [num for num in numbers if num % 2 == 0]

'''
2022 j2
'''