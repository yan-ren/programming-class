# console input and output
# s = input()
# print(s)

# file input and output
# file = open("./input.txt", "r", encoding="utf-8")
# for line in file:
#     print(line, end="")
# file.close()

# with open("./input.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line)
# file.close()
#
# with open("./input.txt", "r", encoding="utf-8") as file:
#     print(file.read(3))
#     print(file.read(5))
# file.close()

with open("./output.txt", "w", encoding="utf-8") as file:
    for row in range(0, 6):
        for col in range(0, row+1):
            file.write("*")
        file.write("\n")
