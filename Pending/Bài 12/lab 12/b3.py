# get user input & write to file
with open('user-inputs.txt', 'w') as wf:
    print("== Input file content below ==")
    while True:
        user_input = input()
        if user_input == "":
            break
        wf.write(user_input + "\n")

# finished input
print('== Input recorded in user-inputs.txt ==')