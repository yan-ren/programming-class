'''
for: iterable item
'''
s = 'abcde'

for letter in s:
    print(letter)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# for i in range(1, 10):
#     print(0)

'''
use for loop print all even number under 20
'''
'''
calculate the sum of 1 to 100
'''
'''
reverse a string
'''
# s = 'abc'
# new_s = ''
# for ch in s:
#     new_s = ch + new_s
#
# print(new_s)

'''
write a program that prints the multiplication table
1x1 = 1
2x1 = 2
2x2 = 4
3x1
3x2
3x3
hint: nested loop
'''
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('*', end='')
#     print()

# for i in range(10, 1, -1):
#     print(i)

'''
Simulated Dice Rolls:
Write a program to simulate rolling a dice 10 times and print the results. 
Use the random module.
In each simulation, print what's the simulation result
after all simulation, print how many times get number 6
'''
# import random
#
# random.randint(1, 6)