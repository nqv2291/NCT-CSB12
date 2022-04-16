print("Give the correct answers to get points.")
score = 0

with open('question-bank.txt') as file:
    # get list of equations
    eq_list = file.readlines()
    
    for question in eq_list:
        # split equation into question and result
        question, result = question.split(",")
        user_ans = input(question)
        if user_ans == result.rstrip():
            score += 1

print(f"== You get {score}/{len(eq_list)} points ==")