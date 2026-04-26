import matplotlib.pyplot as plt

counts = {}

f = open('alice.txt', 'r')

def clean(word):
    '''Strip away leading or trailing punctuation and convert to lower case.'''
    punct = '?!@#$%^&*();:.,\'\"-'
    return word.strip(punct).lower()

for line in f:
    for chunk in line.split():
        for raw_word in chunk.split('--'):
            word = clean(raw_word)
            if word == '':
                continue
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1


f.close()

descending_keys = sorted(counts, key=counts.get, reverse=True)

top_words = descending_keys[:15]
top_freqs = []
for w in top_words:
    top_freqs.append(counts[w])

plt.bar(top_words, top_freqs)
plt.show()