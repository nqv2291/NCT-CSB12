import random

print("\t\t***Freaking Math Game***\n")

# initialize score
score = 0

while True:
    print("Score = {}\n".format(score))
    # Generate random number
    num1 = str(random.randint(0, 50))
    num2 = str(random.randint(0, 50))
    num3 = str(random.randint(-50, 100))

    # Generate random operator
    op = random.choice(("+", "-"))
    
    # Generate question
    equation = f"{num1} {op} {num2}"
    result = (eval(equation) == int(num3))
    print(f"{equation} = {num3} ?")

    # Get user answer
    user_ans = input("True (T) or False (F) ?  ")
    if user_ans.upper() == "T":
        user_ans = True
    elif user_ans.upper() == "F":
        user_ans = False
    else:
        print("[!] Invalid answer -> +0 point\n")
        continue

    # Evaluate answer
    if user_ans == result:
        print("=>> Correct answer. You get +1 point\n")
        score = score + 1
    else:
        print("Ohnoooooooo that's incorrect!!\n")
        break

print("Your score: {}".format(score))