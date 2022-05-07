####################
## EXAMPLE: while loops with the Lost Forest
####################
# n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
# while n == "right" or n == "Right": #RIGHT
#    n = input("\nYou are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
# print("\nYou got out of the Lost Forest!\n\o/")


####################
## EXAMPLE: for loops with Guessing game
####################
# import random
# # randrange() function generates a random integer each time you run the program
# rand_number = random.randrange(10)
# chosen_number = int(input("Guess a number: "))
# if chosen_number == rand_number:
#     print("Waooo, it's totally Correct!!!")
# else:
#     print("The correct answer is {} lew leww".format(rand_number))


####################
## For loops vs While loops
## iterate through numbers in a sequence
####################
## more complicated with while loop
# n = 0
# while n < 5:
#     print(n, end=" ")
#     n = n + 1
# print()

# # shortcut with for loop
# for n in range(5): #(0, 1, 2, 3, 4)
#     print(n, end=" ")




####################
## Debug with VScode debugger
## -> Find the factorial of a number n
####################
# Initialize value of factorial
factorial = 1
n = 5

for i in range(n):
    print("Loop #" + str(i+1))
    print("i =" ,i)
    factorial = factorial*(i+1)
    print("factorial =", factorial)

# Print out final result
print(f"{n}! =", factorial)

