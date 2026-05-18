# # Read the whole file as one string
# with open("notes.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)
#
# # Read line by line (memory-efficient for large files)
# with open("notes.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.rstrip())
#
# with open("notes.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print(lines)


# # Write (overwrites the file if it exists)
# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write("Hello, world!\n")
#     f.write("Second line\n")
#
# # Append (adds to the end)
# with open("output.txt", "a", encoding="utf-8") as f:
#     f.write("Another line\n")
#
# # Write multiple lines at once
# lines = ["apple\n", "banana\n", "cherry\n"]
# with open("fruits.txt", "w", encoding="utf-8") as f:
#     f.writelines(lines)

import json

data = {"name": "Alice", "scores": [90, 85, 92]}

# Write JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["name"])