lst = [75,21,51]
b = int(input("Input new score: "))
lst.append(b)
a=0
print("High scores:")
for i in lst:
    a += 1
    print(a,"-", i)

