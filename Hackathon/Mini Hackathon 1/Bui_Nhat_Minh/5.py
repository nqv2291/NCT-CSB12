import random
print('== FREAKING MATH CONSOLE ==')
print('Give correct answer to get scores.')
print()
score = 0

while True:
    operator = random.choice(['+', '-', '*', '/'])
    if operator == '+' or operator == '-':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    else:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    valid = random.choice(['0', '1'])

    if valid == '0':
        error = error = random.choice([-2, -1, 1, 2])
        answer += error
    if operator == '/':
        num1, answer = answer, num1

    print(f'{num1} {operator} {num2} = {answer}')
    user_answer = input('1 for True, 0 for False: ')
    if user_answer == valid:
        score += 1
        print(f'Score: {score}')
        print()
    else:
        print('Incorrect')
        print()
        break
print('== GAME OVER ==')
print(f'Your total score is {score}.')
