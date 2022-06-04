#import library
import random


#introduce game
print("""--- FREAKING MATH CONSOLE --- 
Give the correct answers to get score. 
    Each correct have 1 point""")

#level
print("""We have 2 level: 
            + First level is 1 to 10
            + second level is 1 to 100""")

#choose level
lvl = int(input("Your level is: "))
    #check lvl
while lvl > 2:
    lvl = int(input("Just have level 1 and level 2, choose again: "))

    #choose the nub for a and b
if lvl == 1:
    lvl1a = 1
    lvl1b = 10
else:
    lvl1a = 1
    lvl1b = 100
#score and check
point = 0
check  = "t"

while check == "t":
        #set the nub
    a = random.randint(lvl1a, lvl1b)
    b = random.randint(lvl1a, lvl1b)
        #set the math symbol 
    sym = random.randint(1,4)

    #print the math
    if (sym == 1):
        print(f"{a} + {b} = ",end=" ")
        pAns = int(input())
        gAns = a + b
    elif (sym == 2):
        print(f"{a} - {b} = ",end=" ")
        pAns = int(input())
        gAns = a - b
    elif (sym == 3):
        print(f"{a} * {b} = ",end=" ")
        pAns = int(input())
        gAns = a * b
    else:
        print(f"{a} / {b} = ",end=" ")
        pAns = int(input())
        gAns = a / b

    if pAns == gAns:
        point += 1
        print(f"Score: {point}")
    else:
        break
print("""
    -- GAME OVER --""")
print(f"Your total score is {point}")
