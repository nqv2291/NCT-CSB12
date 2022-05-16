import turtle as t
n = int(input("Input number of edges: "))
while n < 2:
    print("Error, please enter another number")
    int(input("Input number of edges: "))
else:
    for i in range(n):
        t.forward(100)
        t.left(180 - ((n-2)*180)/n)