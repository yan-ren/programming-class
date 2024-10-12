def revcomp(s):
    s = s.lower()
    reverse_complement = ''
    s = reversed(s)

    for base in s:
        if base == 'a':
            reverse_complement += 't'
        elif base == 't':
            reverse_complement += 'a'
        elif base == 'c':
            reverse_complement += 'g'
        elif base == 'g':
            reverse_complement += 'c'

    return reverse_complement


# print(revcomp('cccgttacggatcc'))
print('abcde', end='')
print('abcde')

def count_stop(dna):
    # Check that the sequence consists of a number of base pairs that is divisible by three
    # if not, your function should simply return -1 to indicate that there is a problem with the data.
    if len(dna) % 3 != 0:
        return -1

    count = 0
    for i in range(0, len(dna) - 3):
        codon = dna[i:i+3]
        # TAG, TAA, and TGA.
        if codon == 'TAG' or codon == 'TAA' or codon == 'TGA':
            count += 1

    if count == 0:
        return -1

    return count


print(count_stop("TTTTATTGACCACGAGATTTATGAATTTACTAGACT"))

'''
return:
1. exit the function
2. give some values to where the function being called
'''

def test(a):
    if a > 0:
        return

    return a


print(test(1))

def federal_tax(income):
    tax = 0

    if income > 235675:
        tax = tax + (income - 235675) * 0.33
        income = 235675
    if income > 165430:
        tax = tax + (income - 165430) * 0.29
        income = 165430
    if income > 106717:
        tax = tax + (income - 106717) * 0.26
        income = 106717
    if income > 53359:
        tax = tax + (income - 53359) * 0.205
        income = 53359

    tax += income * 0.15

    return round(tax, 2)