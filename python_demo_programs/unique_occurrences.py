def unique_occurrences(arr):
    dict = {}
    for num in arr:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    