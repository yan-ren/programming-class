N = int(input())

for _ in range(N):
    line = input()
    count = 1

    # loop through each char in string
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            count += 1
        else:
            print(count, line[i-1], end=' ')
            count = 1

    # print the last group
    print(count, line[len(line) - 1])


list = []
for i in range(5):
    list.append([0] * 5)

list[1][0] = list[0][1]

