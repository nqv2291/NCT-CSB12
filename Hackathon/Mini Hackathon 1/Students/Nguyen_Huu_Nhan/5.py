
import random
print ("Give correct answer to get scores.")
Randomize_sign = 0
Randomize_interger1 = random.randint (1,30)
Randomize_interger2 = random.randint (1,30)
score = 0
 
Randomize_answer = random.randint (-2,2)
if Randomize_sign == 0:
    Answer = Randomize_interger1 + Randomize_interger2 
    Answer = Answer  + Randomize_answer 
    print (f"{Randomize_interger1} +  {Randomize_interger2} = {Answer}")

Answer_input = input("1 for True, 0 for False:")
if Answer_input == 1 and Answer == Randomize_interger1 + Randomize_interger2:
    score = score + 1
    print ("your score is {score}")
elif Answer_input == 0 and Answer != Randomize_interger1 + Randomize_interger2:
    print("Nice")
  
  
  
  

import random
print ("Give correct answer to get scores.")
score = 0
Loop = 0
while Loop == 0:
    Randomize_sign = random.randint (0,2)
    Randomize_interger1 = random.randint (1,30)
    Randomize_interger2 = random.randint (1,30)
    Randomize_answer = random.randint (-2,2)
    if Randomize_sign == 0:
        Answer = Randomize_interger1 + Randomize_interger2 
        Answer = Answer  + Randomize_answer 
        print (f"{Randomize_interger1} +  {Randomize_interger2} = {Answer}")
    elif Randomize_sign == 1:
        Answer = Randomize_interger1 - Randomize_interger2 
        Answer = Answer + Randomize_answer 
        print (f"{Randomize_interger1} - {Randomize_interger2} = {Answer}")
    elif Randomize_sign == 2:
        Answer = Randomize_interger1 * Randomize_interger2 
        Answer = Answer + Randomize_answer 
        print (f"{Randomize_interger1} * {Randomize_interger2} = {Answer}")
    Answer_input = input("1 for True, 0 for False:")
    if Answer_input == str(0) and Randomize_sign == 0:
        if Answer == Randomize_interger1 + Randomize_interger2:
            print ("Incorrect")
            Loop = Loop + 1
        else:
            score = score + 1
            print (f"Your total score is {score}")
    elif Answer_input == str(1) and Randomize_sign == 0:
        if Answer == Randomize_interger1 + Randomize_interger2 :
            score = score + 1
            print (f"Your total score is {score}")
        else:
            print ("Incorrect")
            Loop = Loop + 1
    elif Answer_input == str(0) and Randomize_sign == 1:
        if Answer == Randomize_interger1 - Randomize_interger2:
            print ("Incorrect")
            Loop = Loop + 1
        else:
            score = score + 1
            print (f"Total score is {score}")
    elif Answer_input == str(1) and Randomize_sign == 1:
        if Answer == Randomize_interger1 - Randomize_interger2:
            score = score + 1
            print (f"Total score is {score}")
        else:
            print ("Incorrect")
            Loop = Loop + 1
    elif Answer_input == str(0) and Randomize_sign == 2:
        if Answer == Randomize_interger1 * Randomize_interger2:
            print ("Incorrect")
            Loop = Loop + 1
        else:
            score = score + 1
            print (f" Total score is {score}")
    elif Answer_input == str(1) and Randomize_sign == 2:
        if  Answer == Randomize_interger1 * Randomize_interger2:
            score = score + 1
            print (f"ur score is {score}")
        else:
            print ("Incorrect")
            Loop = Loop + 1
print (f"Your total score {score}")
