#funtion to cal area
def area_of_circle(r):
    result = 3.14*r**2
    return result

r=float(input("input radius:  "))
print("area of circle is ",area_of_circle(r))