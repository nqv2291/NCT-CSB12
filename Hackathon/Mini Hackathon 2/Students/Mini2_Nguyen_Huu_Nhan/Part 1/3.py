colour = ['green','blue','red','white']
print ("Colour list:")
print (*colour, sep = ", ")
New_colour = input("Input a new colour")
colour.append(New_colour)
print ("New colour list:")
print (*colour, sep = ", ")