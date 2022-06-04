score = [78, 70, 67, 56, 45]
a = int(input("Input new score: "))
score.append(a)
score.sort(reverse=True)
print("High scores: ")
for i in range(5):
    print(i+1, ". ", score[i])