import sys
import time

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

def clear_terminal():
    print("\033[H\033[J", end="")

clear_terminal()

def typewriter(text: str, delay: float = 0.01) -> None:
 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    try:
        while True:
            for char in "...":
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)  # Speed
            
            # Backspace 3 times to clear the dots and loop them again
            sys.stdout.write("\b\b\b   \b\b\b") 
            sys.stdout.flush()
    except after 10 seconds:
        pass

    print()

typewriter("Loading")

typewriter(f"{GREEN}-{RED}--------- 10%")
clear_terminal
typewriter(f"{GREEN}---{RED}------- 30%")
clear_terminal
typewriter(f"{GREEN}------{RED}---- 60%")
clear_terminal
typewriter(f"{GREEN}--------{RED}-- 80%")
clear_terminal
typewriter(f"{GREEN}---------{RED}- 90%")
clear_terminal
typewriter(f"{GREEN}---------{RED}- 99%")
clear_terminal
typewriter(f"{GREEN}---------- 100%")
clear_terminal
typewriter(f"{GREEN}OPENING!")
clear_terminal