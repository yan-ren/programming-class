def odd_string(words):
    diff_list = []
    for word in words:
        current = []
        for index in range(len(word) - 1):
            current.append(ord(word[index+1]) - ord(word[index]))
        diff_list.append(current)

    print(diff_list)


odd_string(["adc","wzy","abc"])