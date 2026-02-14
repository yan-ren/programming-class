N = int(input())

max_bid = 0
winner = ''
for _ in range(N):
    name = input()
    bid = int(input())

    if bid > max_bid:
        max_bid = bid
        winner = name

print(winner)