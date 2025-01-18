'''
homework:
2021 J2
'''
N = int(input())
bids = []

for _ in range(N):
    name = input()
    bid = int(input())

    bids.append([name, bid])

# [['Ahmed', 300], ['Suzanne', 500], ['Ivona', 450]]
max_bid = 0
name = ''
for bid in bids:
    # print(bid)
    if bid[1] > max_bid:
        max_bid = bid[1]
        name = bid[0]

print(name)
# numbers = [-1, -2, -3, -1, -5, -2]
# max_number = numbers[0]
#
# for num in numbers:
#     if num > max_number:
#         max_number = num