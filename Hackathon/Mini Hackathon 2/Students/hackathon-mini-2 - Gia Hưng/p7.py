from hashlib import new
from operator import index
from textwrap import indent


score = [ 40 , 80 , 60 , 70 , 90 , 50]
z = 1
while z > 0:
    yesorno = input("new score? write yes or no: ")
    if(yesorno == "yes"):
        newscore = int(input("enter your score: "))
        score.append(newscore)
    if(yesorno == "no"):
        for i in score:
            position = score.index(i) + 1
            print(f"{position}. {i}") 



