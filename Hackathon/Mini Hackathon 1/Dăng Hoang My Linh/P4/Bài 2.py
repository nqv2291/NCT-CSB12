print("==Registration==")
n = input("Username: ")
p1 = input("Password: ")
p2 = input("Repeat password: ")
if p1 == p2:
    input("Email: ")
else:
    print("Password does not match. Please try again.")
    input("Repeat password: ")
    input("Email: ")
print("Registered successfully.")