import sys
import time

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

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
    except KeyboardInterrupt:
        pass

    print()

typewriter("Loading")

typewriter(f"{GREEN}-{RED}--------- 10%")
typewriter(f"{GREEN}---{RED}------- 30%")
typewriter(f"{GREEN}------{RED}---- 60%")
typewriter(f"{GREEN}---{RED}------- 80%")