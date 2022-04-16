Score=[50,100,150]
print("High scores:")
for i in range(0,len(Score)):
    print(f"{i+1}. {Score[i]}")
new=int(input("input new score: "))
Score.append(new)
for i in range(0,len(Score)):
    print(f"{i+1}. {Score[i]}")