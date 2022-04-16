from turtle import *

# get input
while True:
    num_edge = int(input("Enter the number of edges n (n>2): ")) 
    if num_edge > 2:
        break

# draw polygon
for i in range(num_edge):
    forward(100)
    right(360/num_edge)

mainloop()