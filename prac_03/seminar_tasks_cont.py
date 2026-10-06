"""Program to read a file and print only the lines
that start with a # the user should enter the filename
"""

# filename = "Hash_finder.txt"
filename = input("filename?: ")
try:
    in_file = open(filename, "r")
    for line in in_file:
        # print(repr(line))
        line = line.strip()
        # if line.startswith("#"):
        try:
            if line[0] == "#":
                print(line)
        except IndexError:
            continue
    in_file.close()
except FileNotFoundError:
    print("Could not find file")
