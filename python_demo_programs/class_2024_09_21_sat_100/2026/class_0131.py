T, N = map(int, input().split())

for _ in range(T):
    s = input()

    # count frequency of each charactor
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    heavy_light = []
    for ch in s:
        if freq[ch] > 1:
            heavy_light.append(True)
        else:
            heavy_light.append(False)

    # check two possible alternating pattern
    # True False True False
    # False True False True
    option1 = True
    option2 = True

    for i in range(N):
        if heavy_light[i] != (i % 2 == 0):
            option1 = False
        if heavy_light[i] != (i % 2 == 1):
            option2 = False

    if option1 or option2:
        print('T')
    else:
        print('F')