p = int(input()) # "5"
c = int(input()) # "2"

score = p * 50 - 10 * c

if p > c:
    score = score + 500

print(score)