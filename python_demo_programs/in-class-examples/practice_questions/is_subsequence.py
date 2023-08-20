def is_subsequence(s, t):
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    
    s_index = 0
    for ch in t:
        if s_index < len(s):
            if s[s_index] == ch:
                s_index += 1
    
    if s_index == len(s):
        return True
    return False



print(is_subsequence('abc', 'ahbgdc'))
print(is_subsequence("axc", "ahbgdc"))