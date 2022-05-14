username = input("Please input your username to sign up: ")
password = input("Please input your password for the account: ")

b = len(password)
while b<=7:
    print("Password has to have atleast 8 characters")
    password = input("Please input your password for the account: ")

repeatPassword = input("Please repeat the inputed password: ")
while password != repeatPassword:
    print("The password you've entered does not match with the previous one, please try again")
    repeatPassword = input("Please repeat the inputed password: ")

c1 = False
c2 = False
for i in password:
    if i.isalpha:
        c1 = True
    if i.isdigit:
        c2 = True

if (c1 and c2):
    email = input("Please input your email for the account: ")
    while email.find('@') == -1 or email.find('.') == -1:
        email = input("")

print("Registered successfully.")