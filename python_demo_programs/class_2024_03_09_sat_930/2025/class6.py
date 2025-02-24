'''
text = '393HhhUHkbs5gh6QpS-9-8'

uppercase_letters = ''
total_sum = 0
num = ''

for char in text:
    if 'A' <= char <= 'Z':
        if num:
            total_sum += int(num)
            num = ''
        uppercase_letters += char
    elif '0' <= char <= '9':
        num += char
    elif char == '-':
        if num:
            total_sum += int(num)
            num = ''
        num += char
    else: # a - z
        if num:
            total_sum += int(num)
            num = ''
if num:
    total_sum += int(num)

print(uppercase_letters+str(total_sum))
'''

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


s1 = Student('Tom', 12, 'Montreal')
print(s1.name)
# s1.name = 'Tom'
# s1.age = 12
# s1.address = 'montreal'