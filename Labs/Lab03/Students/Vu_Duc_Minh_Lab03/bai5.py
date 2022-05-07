a = input("Please enter your username: ")
b = input("Please enter your password: ")
adbUsername = "admin"
bdbPassword = "123456"
if a == adbUsername and b == bdbPassword:
    print("You're logged in, hello admin.")
else:
    print("Wrong username or password.")