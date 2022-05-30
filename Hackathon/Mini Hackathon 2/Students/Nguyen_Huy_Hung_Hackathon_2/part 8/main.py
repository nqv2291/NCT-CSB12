hi_scores = [78, 56, 67, 43, 32, 22, 19]
inp = int(input("Input new score: "))
hi_scores.append(inp)
hi_scores.sort(reverse=True)
for i in range(len(hi_scores)):
    print(f'{hi_scores.index(hi_scores[i])+1}: {hi_scores[i]}')

inp = int(input("Input new score: "))
hi_scores.append(inp)
hi_scores.sort(reverse=True)
for i in range(5):
    print(f'{hi_scores.index(hi_scores[i])+1}: {hi_scores[i]}')