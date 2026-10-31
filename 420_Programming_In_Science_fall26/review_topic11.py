
# file = open('test.txt')
# context = file.read()
# print('read:', context)
# file.close()

# read file line by line
# file = open('test.txt', 'r')
# for line in file:
#     print('I am reading:', line)

# output_file = open('test.txt', 'a')
# for n in range(10):
#     print(n, file=output_file)
#
# output_file.close()

# f-string
price = input("What's the price for apple?")
count = 9

# text = 'You have total price ' + str(price) + ' for ' + str(count) + ' items'
# text1 = f'You have total price 33.92 for {count} items'
# text2 = f'You have total price 33.92 for {count} items'
# text3 = f'You have total price 33.92 for {count} items'
# text4 = f'You have total price 33.92 for {count} items'
# print(text1)
country = 'US'

s1 = f'You live in {country}'
s2 = f'I live in {country}'
s3 = f'We all live in {country}'