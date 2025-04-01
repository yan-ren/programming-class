def sumabs(lst):
    total = 0
    for x in lst:
        total += abs(x)
    return total

def revcomp(s):
    complement = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c',
                  'A': 't', 'T': 'a', 'C': 'g', 'G': 'c'}
    result = ""
    for base in reversed(s):
        result += complement[base]
    return result.lower()