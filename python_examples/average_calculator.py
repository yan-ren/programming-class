"""
create an average calculator keeps receiving people's input until enter "end"
then calculate the average with all numbers have entered
"""
sum = 0
counter = 0

game_continue = True
while game_continue:
    number = input('enter a number: ')
    if number == 'end':
        print("average: ", sum / counter)
        game_continue = False
    else:
        sum += int(number)
        counter += 1
