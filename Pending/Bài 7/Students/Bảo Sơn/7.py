Score=[50,100,150]
print("Các điểm cao:")
for i in range(0,len(Score)):
    print(f"{i+1}. {Score[i]}")
new=int(input("Thêm điểm: "))
Score.append(new)
for i in range(0,len(Score)):
    print(f"{i+1}. {Score[i]}")