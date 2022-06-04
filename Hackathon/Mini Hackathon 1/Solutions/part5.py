import random

# GAME INTRO
print('\n== FREAKING MATH CONSOLE ==')
print('Give correct answers to get scores.\n')


# GAMEPLAY
score = 0  # user's score

while True:  # while playing
  
  # initialize operations in + - * /
  op = random.randint(0, 3)
  left = None     # left operand
  right = None    # righgt operand
  result = None   # operation result
  op_char = None  # operation character: + - * /

  # randomize operator & operands (toán tử và toán hạng)
  if op == 0:    # ADDITION +
    left = random.randint(0, 50)
    right = random.randint(0, 50)
    result = left + right
    op_char = '+'
  elif op == 1:  # SUBTRACTION -
    left = random.randint(0, 50)
    right = random.randint(0, 50)
    result = left - right
    op_char = '-'
  elif op == 2:  # MULTIPLICATION *
    left = random.randint(0, 10)
    right = random.randint(0, 10)
    result = left * right
    op_char = '*'
  elif op == 3:  # DIVISION /
    right = random.randint(0, 10)
    result = random.randint(0, 10)
    left = right * result  # make sure result is whole number
    op_char = '/'

  # randomize if this expression is correct
  correct_ans = random.randint(0, 1)  # 1 for correct, 0 for incorrect
  if not correct_ans:  # if incorrect, add to result a random number in [-5, -1] and [1, 5]
    result += (random.randint(0, 1)*2-1) * random.randint(1, 5)
  
  # print the expression & get user input
  print(f'{left} {op_char} {right} = {result}')
  print('1 for True, 0 for False: ', end='')
  choice = input()
  if str(correct_ans) == choice:  # if correct answer, increase score & continue game
    score += 1
    print(f'Score: {score}\n')
  else:                           # if incorrect, end the game
    print(f'Incorrect.\n')
    break

# annouce game result
print('== GAME OVER ==')
print(f'Your total score is {score}')