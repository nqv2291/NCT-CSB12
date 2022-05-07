import turtle
a = float(input('Input length 1: '))
b = float(input('Input length 2: '))
c = float(input('Input length 3: '))
if a < b + c and b < c + a and c < a + b:
    if a * a == b * b + c * c or b * b == c * c + a * a or c * c == a * a + b * b:
        print('The 3 line segments can form a right triangle.')
    elif a == b and b == c:
        print('The 3 line segments can form an equilateral triangle.')
        t = turtle.Turtle()
        for i in range(3):
            t.forward(a)
            t.left(120)
        t.screen.mainloop()
    else:
        print('The 3 line segments can form a triangle.')
else:
    print('The 3 line segments cannot form a triangle.')
