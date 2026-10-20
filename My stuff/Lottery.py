import random
import time

import sys

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

def clear_terminal():
    print("\033[H\033[J", end="")

clear_terminal()

speed = random.uniform(0.05,0.1)

def typewriter(text: str, delay: float = (speed)) -> None:
 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

typewriter("Loading . . . \n")

typewriter(f"{GREEN}-{RED}--------- 10%")
time.sleep(0.2)
clear_terminal()
typewriter(f"{GREEN}---{RED}------- 30%")
time.sleep(0.7)
clear_terminal()
typewriter(f"{GREEN}------{RED}---- 60%")
time.sleep(0.4)
clear_terminal()
typewriter(f"{GREEN}--------{RED}-- 80%")
time.sleep(0.8)
clear_terminal()
typewriter(f"{GREEN}---------{RED}- 90%")
time.sleep(0.3)
clear_terminal()
typewriter(f"{GREEN}---------{RED}- 99%")
time.sleep(1.5)
clear_terminal()
typewriter(f"{GREEN}---------- 100%")
time.sleep(2.0)
clear_terminal()
typewriter(f"{GREEN}OPENING!")
time.sleep(0.7)
clear_terminal()


money = 100

while True:
    while True:
        try:
            gamble = int(input("Choose your amount to gamble you have $100 if you get within 5 of the number your invest earns times 4 multiplier if you are within 10 of the number you get 2 times multiplier and if you get within 20 you get 1 multipier if you get within 50 of the number you lose half and anything above that is all the invested money lost.\nBut first choose how much money you want to gamble in the lottery: "))
            if gamble <= 0 or gamble > money:
                print(f"not possible choose between 1 and ${money}.")
                continue
            break
        except ValueError:
            print("Idk what dat is? try again")

    if gamble == money:
        all_in_confirmation = input("Are you sure you want to go all in? type 1 for yes and 2 for no: ")
        if all_in_confirmation == "2":
            continue

    while True:
        try:
            choice = int(input("Choose your number (1-100): "))
            if choice < 1 or choice > 100:
                print("invalid choose between 1 and 100 idiot")
                continue
            break
        except ValueError:
            print("idk what dat is? try again")

    number = random.randint(1, 100)

    jackpot = 1
    while jackpot < number:
        print(jackpot)
        time.sleep(0.1)
        jackpot += 1

    print(f"JACKPOT! The number is . . . {number}!")

    distance = abs(choice - number)

    if distance <= 5:
        multiplier = 4
    elif distance <= 10:
        multiplier = 2
    elif distance <= 20:
        multiplier = 1
    elif distance <= 50:
        money -= gamble // 2
        multiplier = 0
    else:
        money -= gamble
        multiplier = 0
        
    if multiplier > 0:
        money += gamble * multiplier

    print(f"Your number: {choice} | Winning number: {number} | Distance: {distance}")
    print(f"Money remaining: ${money}")
    print()
