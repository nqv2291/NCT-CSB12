name = ["BĐ", "BTL", "CG", "ĐĐ", "HBT" ]
number = [247100, 333300, 266800, 420900, 318000]

print("Indices of: ")
lst = number.copy()
lst.sort()
#lstst num
a = lst[-1]

largest = number.index(a)

print(f"- Most populated dist: {largest}")

#least num
b = lst[0]
least = number.index(b)

print(f"- Least populated dist: {least}")
