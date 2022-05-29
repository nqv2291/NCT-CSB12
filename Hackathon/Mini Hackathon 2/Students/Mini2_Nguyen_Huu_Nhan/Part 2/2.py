colour = ['green','blue','red','white']
print ("Colour list:")
print (*colour, sep = ", ")
input = input("Item to delete:")
if input.isnumeric() == True:
    del(colour[int(input)-1])
    print ("New colour list:")
    print (*colour, sep = ", ")
else:
    colour.remove(input)
    print ("New colour list:")
    print (*colour, sep = ", ")


