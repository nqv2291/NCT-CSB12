lst1 = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
lst2 = [247100, 333300, 266800, 420900, 318000]
maxVal = max(lst2)
maxIndex = lst2.index(maxVal)
minVal = min(lst2)
minIndex = lst2.index(minVal)

# B2
print("Most populated dist:",maxIndex)
print("Least populated dist:",minIndex)
print("")

# B3
print("Most populated dist:",lst1[maxIndex])
print("Least populated dist:",lst1[minIndex])