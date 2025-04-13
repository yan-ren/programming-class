'''
variable: int, float, boolean, string
math operator: + -  * / // % **
boolean operator: and or not
python function:
- input
- print
- random
...

conditional
- if, elif, else
- nested if

loop
- while
- for

function
- def

data structure
- list
- dictionary

class/object
- Arcade

'''

# i = 1
# s = 0
# while i <= 50:
#     s += (i / (51-i))
#     i += 1
#
# print(s)

def sum(numbers):
    s = 0
    for value in numbers:
        s += value

    return s

print(sum([1, 2, 3, 4]))