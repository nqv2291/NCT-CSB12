score = [ 40 , 80 , 60 , 70 , 90 , 50]
scorelist = []
for i in range(len(score)):
    scorelist.append(max(score))
    score.remove(max(score))
print(scorelist)
for i in range(len(scorelist)):
    print(f"{i + 1}: {scorelist[i]}")

for i in range(5):
    print(f"{i + 1}: {scorelist[i]}")