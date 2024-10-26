# This Python program is a number guessing game where the computer selects a secret number between 1 and 10, and the user tries to guess it. The program starts by greeting the user and asking if they want to play the game. If the user says "no," the program ends with a farewell message. If the user says "yes," the program generates a random secret number using the `randint` function from the `random` module. The user is then prompted to guess the number repeatedly. If their guess is too low or too high, the program provides feedback; if the guess is correct, it congratulates the user and ends with a farewell message.

import random

print("Welcome to the Number Guessing Game!")
play_game = input("Would you like to play? (yes/no): ").strip().lower()

if play_game == "yes":
    # Generate a random secret number between 1 and 10
    secret_number = random.randint(1, 10)
    
    while True:
        # Prompt the user to guess the number
        guess = int(input("Guess a number between 1 and 10: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break
    
    print("Thanks for playing! Goodbye!")
else:
    print("Maybe next time! Goodbye!")
