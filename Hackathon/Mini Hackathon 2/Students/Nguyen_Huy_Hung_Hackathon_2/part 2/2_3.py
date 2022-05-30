import turtle 
init = ['blue', 'white', 'red']
turtle.shape('turtle')
turtle.pensize(3)
for i in range(len(init)):
    turtle.color(init[i])
    turtle.down()
    turtle.forward(50)