'''
homework
2023 J2
'''
# N = int(input())
# T = 0
#
# for _ in range(N):
#     chili = input()
#     if chili == 'Polano':
#         T += 1500
#     elif chili == 'Mirasol':
#         T += 6000
#     elif chili == 'Serrano':
#         T += 15500
#     elif chili == 'Cayenne':
#         T += 40000
#     elif chili == 'Thai':
#         T += 75000
#     elif chili == 'Habanero':
#         T += 125000
#
# print(T)

# N = int(input())
# T = 0
# pepper_dic = {
#     'Polano': 1500,
#     'Mirasol': 6000,
#     'Serrano': 15500,
#     'Cayenne': 40000,
#     'Thai': 75000,
#     'Habanero': 125000
# }
#
# for _ in range(N):
#     chili = input()
#     T += pepper_dic[chili]
#
# print(T)

# number_of_players = int(input())
# gold = 0
#
# for _ in range(number_of_players):
#     point = int(input())
#     foul = int(input())
#
#     star = 5*point - 3*foul
#     if star > 40:
#         gold += 1
#
# if gold == number_of_players:
#     print(str(gold) + '+')
# else:
#     print(gold)

d = {'name': 'tom',
     'age': 20}

# check if key exists
if 'name' in d:
    print(d['name'])

# loop each key
for key in d:
    print(key)

# loop key, value
for key, value in d.items():
    print(key, value)