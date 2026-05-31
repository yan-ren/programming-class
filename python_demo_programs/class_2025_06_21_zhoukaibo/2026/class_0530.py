'''
comprehension
'''
numbers = [1, 2, 3, 4]
result = []

for num in numbers:
    if num % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

result = \
    ['even' if num % 2 == 0 else 'odd' for num in numbers]
