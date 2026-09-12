def ask(prompt, retries=4, complaint = "Enter Y/N"):
    for i in range(retries):
        ok = input(prompt)
        if ok in ('Y', 'y'):
            return True
        if ok in ('N', 'n'):
            return False
        print(complaint)
    return False

# ask('really quit?')
# ask('Ok to overwrite the file?', retries=2)
# ask('Update status?', complaint='Just Y/N')
# ask('Send text?', retries=2, complaint='Y/N please!')
# ask('Send text?', retries=2, 'Y/N please!')
# ask('Send text?', retries=2, complaint='Y/N please!')
# ask('Send text?', 2, complaint='Y/N please!')

# variadic positional arguments
def total(*prices):
    print(type(prices), prices)
    return sum(prices)

total(4.99)
total(4.99, 12.5, 3.25)
total()

def scoreboard(player, *rounds):
    return f"{player}: {sum(rounds)} points over {len(rounds)} rounds"

scoreboard("Ana", 10, 15, 7)   # 'Ana: 32 points over 3 rounds'

def total(*prices, tax=0.0):
    return sum(prices) * (1 + tax)

# total(10, 20, 0.15)
total(10, 20, tax=0.15)

# variadic keyword arguments
def describe(**attrs):
    print(type(attrs), attrs)
    for key, value in attrs.items():
        print(f"{key} = {value}")

describe(name="Ana", level=3)

def log_event(event, *tags, **details):
    return f'{event} | tags={tags} | details={details}'

log_event('login', 'web', 'mobile', user='ana', ms=42)

'''
first class functions
functions can be passed as arguments to other functions, returned as the values from other functions and assigned to variables
'''
# functions can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func('Hi, I am a function')
    print(greeting)

greet(shout)
greet(whisper)

# functions can return another function
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder(15)
print(add_15(10))

# functions can be treated as object
def shout(text):
    return text.upper()

print(shout('hello'))

yell = shout
print(yell('hello'))
