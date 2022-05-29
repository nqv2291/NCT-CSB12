score = [78, 56, 67]
a = int(input("Input new score: "))
score.append(a)
score.sort(reverse=True)
print("High scores: ")
for i in range(len(score)):
    print(i+1, ". ", score[i])