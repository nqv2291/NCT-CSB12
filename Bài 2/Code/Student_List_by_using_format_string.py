#Creating rows
row_divider = "+ {:-^3} + {:-^10} + {:-^9} + {:-^7} +".format("","","","")
row_header = "| {:^3} | {:^10} | {:^9} | {:^7} |".format("STT","Họ và tên","Giới tính","Vai trò")
row_0 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("0","Quang Việt","Nam","GV")

row_1 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("1","Vũ Đức Minh","Nam","HS")
row_2 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("2","Uông Minh Đức","Nam","HS")
row_4 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("3","Đặng Hoàng Mỹ Linh","Nữ","HS")
row_5 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("4","Nguyễn Văn Tuấn","Nam","HS")
row_7 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("5","Lưu Gia Hưng","Nam","HS")
row_8 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("6","Bùi Nhật Minh","Nữ","HS")
row_9 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("7","Nguyễn Việt Anh","Nữ","HS")

row_6 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("6","Lê Tiến Vượng","Nam","HS")
row_3 = "| {:^3} | {:<10} | {:^9} | {:^7} |".format("3","Nguyễn Huy Hùng","Nam","HS")
#Print the title
print("\n{:-^39}\n\n".format(" NCT-CSB12 "))

#Table header
print(row_divider)
print(row_header)
print(row_divider)
#Table body
print(row_0)
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)
print(row_6)
print(row_7)
print(row_8)
print(row_divider)