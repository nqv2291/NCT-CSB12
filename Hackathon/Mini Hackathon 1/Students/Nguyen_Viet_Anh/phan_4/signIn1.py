usName = input("Username: ")
psWord = input("Password: ")
mail = input("Email: ")

if (usName == "") or (psWord == "") or (mail == ""):
    print("Registered unsuccess")
else:
    print("Registered successfully")