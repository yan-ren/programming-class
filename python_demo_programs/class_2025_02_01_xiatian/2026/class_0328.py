'''
comprehension
- list
- dictionary
- set
'''
# example: create a list with [1, 4, 9, 16, 25, ..., 100]
# squares = []
# for x in range(10):
#     squares.append(x**2)
#
# squares = [x**2 for x in range(10)]

# sentence = ['and', 'HERE', 'HELLO']
# ['and', 'here', 'hello']
# sentence = ['and', 'HERE', 'HELLO']
# new_sentence = [word.lower() for word in sentence]
#
# seq = [1, 2, 3]
# new_seq = [[x, x**2, x**3] for x in seq]
word = 'Abe'
new_word = []

for ch in word:
    if ch not in 'aeiou':
        new_word.append(ch)

new_word = [ch for ch in word.lower() if ch not in 'aeiou']

numbers = [(i,j) for i in range(5) for j in range(i)]

'''
exercise:
[0, 1, 2, 3] -> [1, 3, 5, 7]
[3, 8, 9, 5] -> [True, False, True, False]
'''