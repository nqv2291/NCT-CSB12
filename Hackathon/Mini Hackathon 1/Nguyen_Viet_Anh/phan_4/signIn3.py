#input
usName = input("Username: ")
psWord = input("Password: ")

#check pass > 8
num = len(psWord)
while num < 8:
    print("Invalid password. Please input again")
    psWord = input("Password: ")
    num = len(psWord)

#input
rePSWord = input("Repeat password: ")

#check password
while psWord != rePSWord:
    print("Passwords not match. Please input again.")
    rePSWord = input("Repeat password: ")

#input
mail = input("Email: ")

#check mail
while mail.find('@') == -1 or mail.find('.') == -1:
    mail = input("Email: ")

#check
if (usName == ""):
    print("Registered unsuccess")
else:
    print("Registered successfully")

