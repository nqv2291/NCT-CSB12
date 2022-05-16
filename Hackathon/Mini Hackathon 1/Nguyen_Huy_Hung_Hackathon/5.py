import random as r
print("== WHAT THE MATH CONSOLE ==\nGive correct answers to get scores.")
print("Note: The results of division will be rounded\nFor example: 9/4 = 2.25 => 2\n")
score = 0

while True:
    operator = r.choice(['+', '-', '*', '/'])
    num1 = r.randint(1, 100)
    num2 = r.randint(1, 100)
    if operator == '/':
        num1 = r.randint(1, 100)
        num2 = r.randint(1, 10)

    if operator == '+':
        answer = int(num1+num2)
    elif operator == '-':
        answer = int(num1-num2)
    elif operator == '/':
        answer = int(num1/num2)
    else:
        answer = int(num1*num2)
    problem = r.randint(answer, answer+20)

    if problem == answer:
        valid = "1"
    else:
        valid = "0"

    print(f"{num1} {operator} {num2} = {problem}")
    user_inp = input("1 for True, 0 for False: ")
    if user_inp == valid:
        score += 1
    else:
        break
print(f"== GAME OVER ==\nYour score is {score}")
