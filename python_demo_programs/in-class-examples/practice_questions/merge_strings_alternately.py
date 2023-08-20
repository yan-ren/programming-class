def one_after_one(w1, w2):
    i = 0
    j = 0
    output = []
    while i < len(w1) or j < len(w2):
        if i < len(w1):
            output.append(w1[i])
            i += 1
        if j < len(w2):
            output.append(w2[j])
            j += 1

    return "".join(output)


print(one_after_one("abcd", "pq"))

l1 = list('abcde')
l2 = 'a,b c d e'.split("")
print(l2)

'''
merge sort
l1 = [1, 2, 5, 6]
l2 = [3, 4]

l3 = [1, 2, 3, 4, 5, 6]

'''
