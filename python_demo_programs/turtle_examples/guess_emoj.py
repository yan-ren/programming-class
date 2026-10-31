import random
import time

emojis = ["🍎", "🍌", "🍇", "🍓", "🍉", "🍒", "🍍", "🥝", "🥭", "🍑"]
original_list = random.sample(emojis, 5)
print(original_list)

time.sleep(3)
print("\n" * 100) # clear the console
# generate 3 incorrect options and shuffle
options = [original_list]
while len(options) < 4:
    shuffled = random.sample(emojis, 5)
    if shuffled not in options:
        options.append(shuffled)

random.shuffle(options)
print('Which one is correct?')
id = 0
for option in options:
    print(id, option)
    id += 1

choice = int(input('Enter the number of the correct option: '))
if options[choice] == original_list:
    print('Correct!')
else:
    print('Wrong')
