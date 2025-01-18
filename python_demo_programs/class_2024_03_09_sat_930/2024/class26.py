'''
number_of_players = int(input())
gold_players = 0

# for value in range(4) ->value [0, 1, 2, 3]
for _ in range(number_of_players):
    score = int(input())
    foul = int(input())

    star = score * 5 - foul * 3
    if star > 40:
        gold_players += 1


if gold_players == number_of_players:
    print(str(gold_players) + '+')
else:
    print(gold_players)
'''

numbers = [1, 2, 3, 4, 5, 6]

result = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(result)

numbers = [-5, 3, 0, 9]
result = ['Positive' if x > 0 else 'Negative' if x < 0 else 'Zero' for x in numbers]

x = 1
if x > 0:
    # append(Positive)
    pass
else:
    if x < 0:
        # append('Negative')
        pass
    else:
        # append('zero)
        pass
    
# 2021 J2
number_of_bids = int(input())
names = []
bids = []

for _ in range(number_of_bids):
    names.append(input())
    bids.append(int(input()))

# hint: max, index
max_bid = max(bids)
max_bid_index = bids.index(max_bid)
print(names[max_bid_index])

# 2020 J2