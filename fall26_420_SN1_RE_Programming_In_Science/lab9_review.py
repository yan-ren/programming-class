'''lab 09 - 2.3
checking password validity
- must not contain any spaces
- at least 10 characters long
- if less than 16, it must pass following additional test:
    - it must contain at least one digit
    - it must contain at least one special character from the set $*&%#

'''

# s = 'a'
# print(s.isdigit())

# if s in '0123456789':

password = input('Enter password: ')

if ' ' in password:
    print('Invalid')

if len(password) < 10:
    print('Invalid')

if len(password) < 16:
    contain_digit = False
    contain_special = False
    for char in password:
        if char.isdigit():
            contain_digit = True
        if char in '$*&%#':
            contain_special = True
    if contain_digit and contain_special:
        print('Valid')
    else:
        print('Invalid')
else:
    print('Valid')