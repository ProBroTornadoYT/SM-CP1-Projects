#GAMES!

import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"

game = input("Type 1 for truth or dare, Type 2 for : ")

if game == '1':
    print(f"{RED}{BOLD} TIME FOR TRUTH OR DARE! {RESET}")
    print(f"{DIM} {ITALIC} {YELLOW} LOADING... {RESET} ")

    answer = random.randint(1,2)

    if answer == 1:
            print(f"{RED}{BOLD} DARE! {RESET}")
    if answer == 2:
        print(f"{GREEN} {BOLD} TRUTH! {RESET}")


