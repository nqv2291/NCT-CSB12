username = input("Tên đăng nhập: ")
email = input("Nhập email: ")
password = input("Mật khẩu: ")
repass = input("Nhập lại pass: ")

while password != repass:
    print("Mật khẩu chưa đúng")
    repass = input("Nhập lại pass: ")

while (email.isalpha()) == False:
    print("Email thiếu dấu @ hoặc .")
    email = ("Nhập lại email: ")

while len(password) < 8:
    print("Pass chưa đủ dài (8 kí tự trở lên)")
    password = ("Nhập lại mật khẩu: ")