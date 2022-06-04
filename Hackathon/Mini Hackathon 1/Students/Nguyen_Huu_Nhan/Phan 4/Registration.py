print ("== Registration ==")
Username = input("Username:")
Password = input("Password:")
Email = input ("Email:")
if Password == str(12345) and Username == "admin" and Email == "abc@gmail.com":
    print ("Registered successfully.")
else:
    print("Wrong pass/email/username")