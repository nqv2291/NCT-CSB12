colour = ['green','blue','red','white']
print ("Colour list:")
print (*colour, sep = ", ")
input = int(input("Input position:"))
print (colour[input-1])