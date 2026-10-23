#SM Fix_game 1

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number:                                       #added ":" defines the loop SOLVED SYNTAX ERROR    
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print(f"Your guesses per round: {scores}")                                  #fixed  the scores "typeerror" error by doing a f string

total = 0

for score in scores:
    total = total + score                                            #removed bunch of loops and extra code and fixed and simplified it

average = total / rounds
print("Your average guesses per round was " + str(average))

best_round = min(scores)                                                    #removed all that scores loop thing and just made it miniumm 

print(f"Your best round took only {best_round} guesses!")


