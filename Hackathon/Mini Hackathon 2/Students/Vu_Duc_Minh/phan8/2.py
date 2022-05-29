lst = [75,21,51,62,12]
b = int(input("Input new score: "))
lst.append(b)
# 2
a = 0
lst.sort()
lst.reverse()
print("High scores:")
for i in lst[:5]:
    a += 1
    print(a,"-", i)
