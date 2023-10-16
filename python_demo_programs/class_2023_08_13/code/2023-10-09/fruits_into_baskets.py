def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_freq = {}

    for window_end in range(len(fruits)):
        right = fruits[window_end]
        if right not in fruit_freq:
            fruit_freq[right] = 1
        fruit_freq[right] += 1

        while len(fruit_freq) > 2:
            left = fruit_freq[window_start]
            fruit_freq[left] -= 1
            if fruit_freq[left] == 0:
                del fruit_freq[left]
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)

    return max_length