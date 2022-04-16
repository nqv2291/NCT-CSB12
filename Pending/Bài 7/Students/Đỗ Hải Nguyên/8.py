Score=[50,100,150,200,250]
new=int(input("input new score: "))
Score.append(new)
Score.sort()
for i in range(0,5):
    print(f"{i+1}. {Score[i]}")