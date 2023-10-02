def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_length = 0
    char_freq = {}

    for window_end in range(len(str)):
        end_char = str[window_end]
        if end_char not in char_freq:
            char_freq[end_char] = 0
        char_freq[end_char] += 1

        while len(char_freq) > k:
            start_char = str[window_start]
            char_freq[start_char] -= 1
            if char_freq[start_char] == 0:
                del char_freq[start_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


print(longest_substring_with_k_distinct('araaci', 2))
