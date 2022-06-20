import sys

if len(sys.argv) < 2:
    print("Usage: main.py FILE_WANTED_TO_EDIT")
    sys.exit(1)

f = open(sys.argv[1])

# firstLine = f.readline()
# print(firstLine)

for line in f:
    print(line)

f.close()








