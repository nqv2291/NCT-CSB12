import math
#1
x = int(input("Input first number:"))
y = int(input("Input second number:"))
print(x, "+", y, "=", x+y, sep=" ")

#2
a = int(input("Input a:"))
b = int(input("Input b:"))
c = int(input("Input c:"))
print("\n")
if (a == 0):
    if (b == 0):
        print ("This equation has no solution.")
    else:
        print ("This equation has 1 solution: x = ", + (-c / b))

delta = b * b - 4 * a * c
if (delta > 0):
    x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
    x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
    print ("The equation has 2 solutions: x = ", x1, " and x = ", x2)
elif (delta == 0):
    x1 = (-b / (2 * a))
    print("The equation has 1 solution: x1 = x2 = ", x1)
else:
    print("The equation has no solution.")

#3
def is_palindrome(a):
    b=a[::-1]
    if b == a:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")

x = input("Input a text:")
is_palindrome(x)

#4
print("== Welcome to MindX Restaurant ==\n")

food_list= []

x = input("Please choose a dish:")
food_list.append(x)
y = input("Great choice! Anything else? (Y/N):")
print("\n")
if y == "y":
    while y == "y":
        x = input("Please choose a dish:")
        food_list.append(x)
        y = input("Great choice! Anything else? (Y/N):")
        print("\n")
if y == "n":
    print("Well done! Your order:", *food_list, sep="\n -")

#5
Phone_dict = {
    "Iphone 12" : 28000000,
    "Samsung N10" : 16000000,
    "Oppo 93" : 7500000,
    "Vsmart" : 7400000,
    "Vivo" : 4200000,
}

x = input("Input name of a phone:")
print("Price of", x, ":", Phone_dict[x])

y = int(input("Input your budget:"))
if y >= 28000000:
    print("Phones that fit your budget:")
    print("\n".join("-{}: {}".format(k, v) for k, v in Phone_dict.items()))
elif y>= 16000000 and y< 28000000:
    Phone_dict.pop("Iphone 12")
    print("Phones that fit your budget:")
    print("\n".join("-{}: {}".format(k, v) for k, v in Phone_dict.items()))
elif y>= 7500000  and y< 16000000:
    Phone_dict.pop("Iphone 12")
    Phone_dict.pop("Samsung N10")
    print("Phones that fit your budget:")
    print("\n".join("-{}: {}".format(k, v) for k, v in Phone_dict.items()))
elif y>= 7400000 and y< 7500000:
    Phone_dict.pop("Iphone 12")
    Phone_dict.pop("Samsung N10")
    Phone_dict.pop("Oppo 93")
    print("Phones that fit your budget:")
    print("\n".join("-{}: {}".format(k, v) for k, v in Phone_dict.items()))
elif y>= 4200000 and y< 7400000:
    Phone_dict.pop("Iphone 12")
    Phone_dict.pop("Samsung N10")
    Phone_dict.pop("Oppo 93")
    Phone_dict.pop("Vsmart")
    print("Phones that fit your budget:")
    print("\n".join("-{}: {}".format(k, v) for k, v in Phone_dict.items()))
else:
    print("Phones that fit your budget:")
    print("None")

#6
x = int(input("Input a number:"))
y= str(x)
print("The number has", len(y), "digits", sep=" ")

#7
orginial_list = [5, 1, 8, 92, -1, 30]
print("Original list:", "\n", *orginial_list)
for i in range(len(orginial_list)):
    for j in range(i + 1, len(orginial_list)):

        if orginial_list[i] > orginial_list[j]:
           orginial_list[i], orginial_list[j] = orginial_list[j], orginial_list[i]

print("Sorted list:", "\n", *orginial_list)

#8
x = int(input("Input a number:"))
Fibonacii = [1, 1]
for i in range(x-2):
    t = Fibonacii[i] + Fibonacii[i+1]
    Fibonacii.append(t)

print("First", x,"Fibonacii numbers:", *Fibonacii)