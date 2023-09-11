def smalleset_subarray_with_given_sum(list, s):
    window_sum = 0
    min_length = len(list)
    window_start = 0

    for window_end in range(len(list)):
        window_sum += list[window_end]
        # shrink the window as small as possible unitl the window_sum is smaller than s
        while window_sum > s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= list[window_start]
            window_start += 1
    
    return min_length
