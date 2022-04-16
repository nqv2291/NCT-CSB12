my_str = input("Nhập chuỗi: ")
my_str = my_str.casefold()
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("Đây là chuỗi palindrome.")
else:
   print("Đây không phải chuỗi palindrome.")