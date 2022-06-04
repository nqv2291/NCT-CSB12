print ("== Registration ==")
Username = input("Username:")
Password = input("Password:")
while len(Password) < 8 :
    print ("Invalid password")
    Password = input("Password:")
Repeat_Password = input("Repeat_Password:")
while Repeat_Password != Password:
    print ("Passwords not match. Please input again.")
    Repeat_Password= input("Repeat_Password:")
Email = input ("Email:")
while Email.count(".") == 0 or Email.count("@") == 0:
    print ("Invalid email")
    Email = input ("Email:")
if len(Password) >= 8 and Username == "admin" and Email == "abc@gmail.com":
    print ("Registered successfully.")