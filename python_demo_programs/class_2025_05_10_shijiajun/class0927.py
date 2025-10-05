import random

# lower = int(input('Enter the lower range for guessing:'))
# upper = int(input('Enter the upper range for guessing:'))
# target = random.randint(lower, upper)
# chance = 3
#
# while chance > 0:
#     guess = int(input('Guess a number between 0 to 20'))
#
#     if guess > target:
#         print('Too high')
#     elif guess < target:
#         print('Too low')
#     else:
#         print('Correct')
#         exit(0)
#
#     chance -= 1

# followup question: using input function to ask user to give a random range

# multiplication quiz

chance = 3
marks = 0

while chance > 0:
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    correct_answer = num1 * num2

    guess = int(input(f'What is {num1} * {num2}?'))
    if guess == correct_answer:
        print('Correct!')
        marks += 1
    else:
        print('Wrong!')

    chance -= 1

print('Total marks:', marks)
'''
improve
- let people answer 3 questions
- if answer correctly, get 1 mark, show the total marks when program finishes
'''