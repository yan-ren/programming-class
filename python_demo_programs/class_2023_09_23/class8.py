def welcome(name):
    print('welcome', name)


def greeting(msg, name):
    print(msg, name)


def question(option):
    if option == 1:
        print('question 1: what is your name')
    elif option == 2:
        print('question 2: where do you live')
    elif option == 3:
        print('question 3: how old are you')

    answer = input('enter answer')
    if option == 3 and int(answer) == 10:
        print('you are 10 age')
    else:
        print()

# question(3)
# welcome('Tom')
# welcome('Jerry')
# welcome()

# greeting('hello', 'Tom')

def q_and_a():
    print('you are facing two doors, door 1 and door 2')
    answer = input('which one do you choose: ')
    if answer == '1':
        print('there is a bear')
        answer = input('what do you do: 1. feed it. 2. pet it')
        if answer == '1':
            print('The bear is full')
        elif answer == '2':
            print('The bear is happy')
    elif answer == '2':
        print('there is a tiger')
    else:
        print('option does not exist')


q_and_a()

def addition(a, b):
    return a + b


print(addition(1, 2))