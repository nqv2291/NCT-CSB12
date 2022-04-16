from datetime import datetime

# get user input & write to file
with open('input-logs.txt', 'a') as wf:
    print("== Input file content below ==")
    # record input time
    time_current = datetime.now()
    wf.write(f"== Inputs at {time_current} ==\n")

    while True:
        user_input = input()
        if user_input == "":
            break
        wf.write(user_input + "\n")   
    wf.write("\n")
# finished input
print("== Input recorded in input-logs.txt ==")