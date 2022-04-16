name=input('ten dang nhap: ')
email=str(input("email: "))
while email.find("@gmail.com")==-1:
   print("email phai chua @gmail.com")
   email=input("email: ") 
password=input("password: ")
while len(password)<8 or password.isdigit()== True or password.isalpha()== True :
    print('password phai toi thieu 8 ky tu va chua ky tu voi so')
    password=input("password: ")
conPass=input("confirm password: ")
while password != conPass:
    print("cofirm password and password do not match")
    conPass=input("confirm password: ")