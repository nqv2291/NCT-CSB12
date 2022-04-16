radius = float(input("Enter radius: "))

def area_of_circle(radius):
    area = 3.14*radius*radius
    return area

print("Area of circle of radius " + str(radius) + " is: ", area_of_circle(radius))
