# 1.
colour = ['green','blue','red','white']
print ("Colour list:")
print (*colour, sep = ", ")
input = int(input("Input position:"))
print (colour[input-1]) 
# 2.
# 3.
import turtle
color_list = ['red', 'green', 'blue', 'yellow', 'orange',
              'purple', 'pink', 'brown', 'black', 'white']
turtle.shape('turtle')
turtle.pensize(3)
turtle.penup()
turtle.backward(200)

for i in range(len(color_list)):
    turtle.color(color_list[i])
    turtle.down()
    turtle.forward(50)
    turtle.penup()
    turtle.forward(25)
turtle.color('black')
turtle.mainloop()