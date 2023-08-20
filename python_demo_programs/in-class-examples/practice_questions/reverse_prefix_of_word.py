s = 'abcdef'
print(s[0])
print(s[0:3])

print(s.index("d"))


def reverse_prefix_of_word(word, ch):
    if ch not in word:
        return word
    
    index = word.index(ch)
    prefix = word[0:index+1]
    prefix = prefix[::-1]

    return prefix + word[index+1:]


print(reverse_prefix_of_word("abcdefd", "d"))
