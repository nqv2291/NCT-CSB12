import os
# get file name
file_name = input("Input file name: ")

# check if file exists & get file content
if os.path.exists(file_name):
    with open(file_name) as rf:
        print("File content:")
        print(rf.read(), end='')
else:
    print("File not found.")