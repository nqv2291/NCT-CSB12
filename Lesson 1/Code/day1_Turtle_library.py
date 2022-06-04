#Gọi thư viện turtle bằng cú pháp sau
from turtle import *
import
#Ví dụ vài đường cơ bản

shape('turtle')
color('red')
pensize(6)

for i in range(5):
    forward(300)
    right(144)

#Thêm dòng lệnh sau để cửa sổ vẽ hình của Turtle không bị tự động đóng sau khi vẽ xong
mainloop()