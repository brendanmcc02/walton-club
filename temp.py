import random as rd

print("Random Number Guessing Game!")

ans = rd.randint(1, 10)

for i in range(1,6):
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == ans:
        print("Correct! You win!")
        break

    print("Incorrect! " + str(5-i) + " turns remaining")

print("You lose!")
