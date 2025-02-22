'''
int
float
boolean
string
'''
# a = 1
# b = str(a)
#
# a = '123'
# # a = a + 1 # cannot be calculated as int, need convert before calculation
# b = int(a)
# b = float(a)
#
# print(a, b, sep='')
# print("J'aime", "les maths") # print two values, the space is added by print function by default
# print("J'aime " + "les maths") # combine into one value, the space is given by us

# input() # input function takes everything as string
'''
+ - * / // ** %
'''
# import math
#
#
# print(math.sqrt(4))
#
# a = (1+2)*3

# option 1: using string property
# phone_num = input('Enter your phone number:')
# print(phone_num[0] + phone_num[1] + phone_num[2])

# option 2: use math, assume ten digits
# phone_num = int(input('Enter your phone number:'))
# area_code = phone_num // 10**7 # divide to remove the last 7 digits
# print(area_code)

phone_number = 5144303333
country_code = 1
area_code = 514

# print('The country code is', country_code, ', phone number is', phone_number, ', area_code', area_code)
# # print with format
# print(f'The country code is {country_code}, phone number is {phone_number}, area code is {area_code}')
# distance = float(input('Enter the distance:'))
# time = int(input('Enter the time:'))
#
# distance_meters = distance * 1000
# time_seconds = time * 60
# speed_per_s = distance_meters / time_seconds
#
# hours = time // 60
# minutes = time % 60
#
# print(f'The travel time is {hours}h et {minutes}m.')
x = 1234
# print(x % 10) # gives the right most digit
# # print(x // 10) # removes the right most digit
#
# x = x // 10 # 123
# print(x % 10)
# x = x // 10 # 12
# print(x % 10)
# x = x // 10
# print(x % 10)

while x > 0:
    print(x % 10) # takes the right most digit
    x = x // 10 # remove the right most digit
