def welcome_message():
    print('welcome, are you ready for a question?')


def question():
    # welcome_message()
    answer = input("what's your name?")
    print('your answer:' + answer)


# call the function
welcome_message()
question()