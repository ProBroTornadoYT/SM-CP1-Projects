# Password Strentgh Checker SM 1

import sys
import time

def typewriter(text: str, delay: float = 0.04) -> None:
    """Prints text character by character without color or formatting."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    print()

# Color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
BRIGHT_BLACK= '\033[90m'
BRIGHT_RED= '\033[91m'
BRIGHT_GREEN= '\033[92m'
BRIGHT_YELLOW= '\033[93m'
BRIGHT_BLUE= '\033[94m'
BRIGHT_MAGENTA= '\033[95m'
BRIGHT_CYAN= '\033[96m'
BRIGHT_WHITE= '\033[97m'
BROWN = '\033[38;5;94m'
MAROON = '\033[38;5;88m'
CRIMSON = '\033[38;5;160m'
CORAL = '\033[38;5;209m'
PEACH = '\033[38;5;216m'
OLIVE = '\033[38;5;100m'
LIME_GREEN = '\033[38;5;46m'
FOREST_GREEN = '\033[38;5;22m'
AQUA = '\033[38;5;51m'
SKY_BLUE = '\033[38;5;117m'
NAVY_BLUE = '\033[38;5;18m'
INDIGO = '\033[38;5;54m'
VIOLET = '\033[38;5;129m'
PLUM = '\033[38;5;96m'
MAGENTA = '\033[38;5;201m'
DARK_GRAY = '\033[38;5;236m'
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
INVERT = "\033[7m"
STRIKE = "\033[9m"

import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

def clear_terminal():
    print("\033[H\033[J", end="")

clear_terminal()

speed = random.uniform(0.05,0.06)

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


password = input("Enter Password: ")

strength = 0

chars = list(password)
if any(char.islower() for char in chars):
    strength += 1

chars = list(password)
if any(char.isupper() for char in chars):
    strength += 1

chars = list(password)
if any(char.isdigit() for char in chars):
    strength += 1

special_chars = ['!','@','#','$','%','^','&','*','(',')','_','+','-','=','[',']','{','}','|',';',':',',','.','<','>','?']
if any(char in special_chars for char in chars):
    strength += 1

if len(password) >= 8:
    strength += 1

final_strength = (strength)*13.4

typewriter(f"{RESET}Your strength Index is: \n")
typewriter(str(final_strength))

if final_strength == 13.4:
    typewriter(f"\nPassword Strength is {RED}{BOLD}TOO WEAK{RESET} try again")

if final_strength == 26.8:
    typewriter(f"Password Strength is {RED}{BOLD}Weak try{RESET} again")

if final_strength == 40.2:
    typewriter(f"Password Strength is {YELLOW}{BOLD}Medium{RESET} try again")

if final_strength == 53.6:
    typewriter(f"Password Strength {YELLOW}Could be improved{RESET} try again")

if final_strength == 67:
    typewriter(f"Password Strength is {GREEN}{BOLD}GREAT!")

