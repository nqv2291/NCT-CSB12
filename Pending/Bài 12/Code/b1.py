print("List of names:")
with open("names.txt", "r") as f:
    for i in range(3):
        line = f.readline()
        print("- " + line, end="")