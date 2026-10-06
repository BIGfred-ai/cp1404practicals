"""Program for removing names from a list"""

names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove? ")
while name_to_remove != "":
    # print(name_to_remove)
    # del names [0]
    try:
        names.remove(name_to_remove)
    except ValueError:
        pass
    name_to_remove = input("Who do you want to remove?")
print(", ".join(names))


