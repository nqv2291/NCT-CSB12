print("\t\t***Registration Simulation v3.0***\n")
print("Create your Hacker account")

# get username
username = input("Username: \t ")

# get password
while True:
    password = input("Password: \t ")

    # check password length (> 8)
    if len(password) < 8:
        print("[!] Use 8 characters or more for your password")
        continue

    # check password included both digits and letters
    if password.isalpha() or password.isdigit():
        print("[!] Choose a stronger password. Try a mix of letters and numbers")
        continue

    # confirm password
    password_cf = input("Verify password: ")
    if password == password_cf:
        break
    else:
        print("[!] Those password didn't match. Try again")

# get email
while True:
    email = input("Email:\t\t ")
    if ("@" in email) and ("." in email) and (" " not in email):
        break
    else:
        print("[!] A valid email must include @ and . without any blank space")

print("\nSign up complete. Welcome abroad!")