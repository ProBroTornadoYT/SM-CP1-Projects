#the gusseing game by copilot

import random
def mini_game():
    print("Mini Game: Rock, Paper, Scissors")
    choices = ["rock", "paper", "scissors"]

    player = input("Choose rock, paper, or scissors: ").lower()
    if player not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a draw!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

mini_game()

def play_game():
    secret_number = random.randint(1, 20)
    max_attempts = 5
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 20.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return

    print(f"Sorry! The number was {secret_number}.")
    print("Better luck next time!")

while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
