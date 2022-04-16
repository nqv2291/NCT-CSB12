import turtle
color=["blue","red","green"]
read=int(input("Input position: "))
print(color[read-1])
dell= input("item to delate: ")
if dell.isdigit() == True:
    dell=int(dell)
    del(color[dell-1])
else:
    color.remove(dell)
print("new color list: ")
for i in range(0,len(color)):
    print(color[i],end=", " )
    turtle.shape("turtle")
for i in range(0,len(color)):
    turtle.color(color[i])
    turtle.pencolor(color[i])
    turtle.forward(100)
    turtle.penup()
    turtle.forward(50)
    turtle.penup()
    turtle.pendown()
turtle.mainloop()