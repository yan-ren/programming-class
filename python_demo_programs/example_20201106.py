# Print out the first n Fibonacci numbers
def fibbi1(n):
    a, b = 0, 1
    index = 0


# fibb(5) -> 0, 1, 1, 2, 3
def fibbi2(n):
    l = []
    l.append(0)
    l.append(1)
    # [0, 1]
    index = 2
    while index <= n:
        l.append(l[index - 1] + l[index - 2])
        index += 1
    print(l)


def quick_maths(a, b, c):
    return a + b - c


boom = (1, 1, 1)
quick_maths(*boom)

# [] () {}
# pair 2->"two"
# one pair has one key : one value
sample = {0: "Yan", 1: "Gary", 2: "Gilbert", 3: "Hangbing", 4: "Justin", 5: "Nick", 6: "Yijun Zhu"}
print(sample[20])

# in school we have student ID -> student name
# studentID is the key
# student name is the value