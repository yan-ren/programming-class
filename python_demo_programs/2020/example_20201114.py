# homework: create a dictionary using loop,
# where the sum of each key and value equals to 10
# example:
# d = {0: 10, 1:9, 2: 8, 3: 7, 4: 6, 5:5, 6:4, 7:3, 8:2, 9:1, 10:0}

d = {1: 100}
d[1] = 200
d[2] = 100
print(d)

# give a list of names, create a dictionary where the key is the family and value is the list of full name
# whose family name is the same

l = ["Aaron Hank", "Abagnale Frank", "Abbey Edward", "Abel Frank"]
d = {"Hank" : ["Aaron Hank"], "Frank": ["Abagnale Frank", "Abel Frank"], "Edward": ["Abbey Edward"]}

for i in l:
    items = i.split()
    print(items)

