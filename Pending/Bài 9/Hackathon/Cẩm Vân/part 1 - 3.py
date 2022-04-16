a_string = str(input("Nhập một string: "))

# đảm bảo các chữ cái in thường 
a_string = a_string.lower().replace(' ', '')

def string_reverse(): 
# đảo ngược các kí tự trong chuỗi 
   a_reversed_string = ''.join(reversed(a_string))
   return a_reversed_string

print(string_reverse())