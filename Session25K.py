file = open("students.csv", "r")
lines = file.readlines()
for line in lines:
    data = line.split(",")
    print(data[0], data[1])

print("```````````````")

source_code = open("Session25I.py", "r")
source_code_lines = source_code.readlines()
for line in source_code_lines:
    print(line)

# Count how many classes and functions are created in a source code :)