# THE NUMBER GUESSING GAME
#  In the number guessing game, the program selects a random number between two numbers, and the user guesses the correct number
import random

number = random.randint(1, 100)
attempt = 1
guess = int(input("Enter A Number:"))
while True:
    if guess > number:
        guess = int(input("The Number You Guessed Is Large,Go For Lesser One:"))
        attempt += 1
    elif guess < number:
        guess = int(input("The Number You Entered Is Small,Go For Larger Number:"))
        attempt += 1
    else:
        print(f"You Guessed It Right In {attempt} attempts")
        break
