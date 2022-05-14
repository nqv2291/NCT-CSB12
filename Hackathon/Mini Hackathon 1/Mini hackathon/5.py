#chua xong cho em them thoi gian::((
import random
print ("give correct answer")
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