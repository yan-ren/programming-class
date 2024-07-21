'''
More about function
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]

def merge_lists(l1, l2):
    new_list = []
    for value in l1:
        new_list.append(value)

    for value in l2:
        new_list.append(value)

    return new_list

# print(merge_lists(list1, list2))

# function takes a string as input and return how many vowels in the string
def vowel_char_counter(s):
    count = 0
    for letter in s:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count += 1

    return count



def calculator():
    running = True

    while running:
        print('Welcome to the calculator program')
        num1 = float(input('Enter the first number for calculation: '))
        print('Available operation: + - * /')
        operation = input('Pick an operation:')
        num2 = float(input('Enter the second number for calculation: '))

        if operation == '+':
            print(f'{num1} {operation} {num2} = {num1 + num2}')
        elif operation == '*':
            print(f'{num1} {operation} {num2} = {num1 * num2}')
        elif operation == '-':
            print(f'{num1} {operation} {num2} = {num1 - num2}')
        elif operation == '/':
            print(f'{num1} {operation} {num2} = {num1 / num2}')

        choice = input('do you want another calculation? y/n')
        if choice:
            running = True
        else:
            running = False

    # exercise: after done with calculation ask user if wants to do another calculation, if yes, continue with another calculation
    # if no, exit the program
    # hint: use loop

calculator()