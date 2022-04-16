print("\t\t***Registration Simulation v2.0***\n")
print("Create your Hacker account")

# get username
username = input("Username: \t ")

# get password
while True:
    password = input("Password: \t ")
    password_cf = input("Verify password: ")
    if password == password_cf:
        break
    else:
        print("[!] Those password didn't match. Try again")

# get email
email = input("Email:\t\t ")

print("\nSign up complete. Welcome abroad!")