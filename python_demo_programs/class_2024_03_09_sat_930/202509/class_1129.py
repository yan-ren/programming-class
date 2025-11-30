'''
string
if statement
loop:
 - while
 - loop
def

list
 - 2d list
dictio
set

comprehension
recursion
----
class
'''
X = int(input())

same = []
for _ in range(X):
    data = input().split()
    same.append([data[0], data[1]])

diff = []
Y = int(input())
for _ in range(Y):
    data = input().split()
    diff.append([data[0], data[1]])

# print(same)
# print(diff)
G = int(input())
team = {}
for _ in range(G):
    group = input()
    items = group.split()
    team[items[0]] = group
    team[items[1]] = group
    team[items[2]] = group

# print(team)
count = 0
for pair in same:
    if team[pair[0]] != team[pair[1]]:
        count += 1

for pair in diff:
    if team[pair[0]] == team[pair[1]]:
        count += 1

print(count)