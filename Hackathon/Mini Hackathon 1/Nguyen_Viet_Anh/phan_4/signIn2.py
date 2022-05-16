usName = input("Username: ")
psWord = input("Password: ")
mail = input("Email: ")

#check password
while psWord != rePSWord:
    print("Passwords not match. Please input again.")
    rePSWord = input("Repeat password: ")
#check input
if (usName == "") or (psWord == "") or (mail == ""):
    print("Registered unsuccess")
else:
    print("Registered successfully")