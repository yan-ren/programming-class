'''
2015 j4
'''

n = int(input())

start_time = {}
wait_time = {}
waiting = []

current_time = 0

for _ in range(n):
    parts = input().split()
    if parts[0] == 'R':
        friend = int(parts[1])
        start_time[friend] = current_time
        if friend not in wait_time:
            wait_time[friend] = 0
        waiting.append(friend)
        current_time += 1
    elif parts[0] == 'S':
        friend = int(parts[1])
        if friend in waiting:
            wait_time[friend] += (current_time - start_time[friend])
            waiting.remove(friend)
        current_time += 1
    elif parts[0] == 'W':
        time = int(parts[1])
        current_time -= 1
        current_time += time

for friend in sorted(wait_time.keys()):
    if friend in waiting:
        print(friend, -1)
    else:
        print(friend, wait_time[friend])

