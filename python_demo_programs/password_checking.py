password = input("enter a password")

index = 0
lowercase = uppercase = numbers = special = 0
# lowercase = 0

while index < len(password):
    if 'a' <= password[index] <= 'z':
        lowercase += 1
    elif 'A' <= password[index] <= 'Z':
        uppercase += 1
    elif '0' <= password[index] <= '9':
        numbers += 1
    else:
        special += 1
    index += 1

if lowercase > 0 and uppercase > 0 and numbers > 0 and special > 0:
    print('valid password')
else:
    print('non valid password')