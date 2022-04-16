import random
import operator

def quiz():

    print('Welcome. This is a math quiz\n')
    name = input("Please enter your name: ")
    print("Hello", name," Let's begin the quiz!")
    score = 0
    for i in range(20):
        correct = askQuestion()
        if correct:
            score += 1
            print('Correct!')
            print ("Score",(score),"\n")
        else:
            print('Incorrect!')
            print ("Score",(score), "\n")

    print ('Your score was {}/20'.format(score))


def askQuestion():
    answer = randomCalc()
    guess = float(input())
    return guess == answer

def randomCalc():
    ops = {'+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv}
    num1 = random.randint(0,50)
    num2 = random.randint(1,50)   
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print('What is {} {} {}?'.format(num1, op, num2))
    return answer

quiz()
#askQuestion()
#randomCalc()









from sys import exit 
counter = 0 
print("Question 1.") 
print ("2 + 3 = ?") 
answer_one = input("> ") 
 
if answer_one == "5": 
    print ("Correct!") 
    counter += 1 
else: 
    print("Wrong!") 
 
print (" ") 
print ("Question 2.") 
print ("2 + (2 / 2) = ?")
answer_two = input("> ") 
 
if answer_two == "3": 
    print ("Correct!") 
    counter += 1 
else: 
    print ("Wrong!") 
 
print (" ") 
print ("Question 3.") 
print ("x - 4 = ?")
answer_three = input("> ") 
 
if answer_three == "4": 
    print ("Correct!")
    counter += 1 
else: 
    print ("Wrong!")
 
print (" ") 
print ("Result: %d correct answers out of 3" % counter)
exit(0) 