#love tester

import random

import sys
import time
import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

"""def clear_terminal():
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
"""

person1 = input("Type your first person: ").strip().title()
person2 = input("Type your second person person: ").strip().title()

love = random.randint(70,120) 

print(f"Looks like {person1} loves {person2} at about {love}% love oooh")

if love > 100:
    print(f"Oh dayum {love}% love is more than 100! thats a match made in heaven")

if love == 120:
    print("120 percent!!!!!! thats THE MAX AMOUNT OF LOVE!!!!")