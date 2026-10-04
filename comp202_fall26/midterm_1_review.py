# short answer 3
def rectangle_area(side1, side2):
    area = side1 * side2
    return area

# short answer 4
def get_middle(a, b, c, d, e):
    # find and put the smallest value in a
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if a > e:
        a, e = e, a

    # exclude a, find the smallest value from b, c, d, e and put it in b
    if b > c:
        b, c = b, c
    if b > d:
        b, d = d, b
    if b > e:
        b, e = e, b

    # exclude a and b, find the smallest value from c, d, e and put it in c
    if c > d:
        c, d = d, c
    if c > e:
        c, e = e, c

    return c

# short answer 5
play_again = 'Y'

while play_again != 'N':
    user_move = input('Enter Rock, Paper, Scissors: ')
    if user_move == 'Rock':
        computer_move = 'Paper'
    elif user_move == 'Paper':
        computer_move = 'Scissors'
    else:
        computer_move = 'Rock'

    print('You chose:', user_move)
    print('I choose:', computer_move)
    print('I win!')

    play_again = input('Play again? (Y/N)')

# long answer 1
slices = int(input('How many slices are available?'))
people = int(input('How many people?'))

person = 1
stop = False

while slices > 0 and not stop:
    people_left = people - person + 1

    if slices < people_left:
        max_allowed = 1
    else:
        max_allowed = slices // people_left

    wanted = int(input('How many wanted?'))
    if wanted == -1:
        stop = True
        break

    while wanted > max_allowed:
        print('Too many wanted!')
        print('Enter a lower number')
        wanted = int(input('How many wanted?'))
        if wanted == -1:
            stop = True
            break

    if stop:
        break

    slices -= wanted
    print('Slices remaining:', slices)

    person += 1
    if person > people:
        person = 1

print('Program finished!')