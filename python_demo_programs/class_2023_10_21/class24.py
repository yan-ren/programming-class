'''
CCC2023 J1
'''
package = int(input())
obstacle = int(input())
score = 0

if package > obstacle:
    score = 500

score = score + package * 50
score = score - obstacle * 10

print(score)
