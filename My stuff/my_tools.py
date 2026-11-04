import time
import random

# Color codes for the terminal
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"  # Stops the color from bleeding into the rest of the terminal

def greet(name):
    return f"Hello, {name}!"

def typewriter(text):
    """Helper function to print text letter by letter."""
    speed = random.uniform(0.03, 0.07)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)

def clear_terminal():
    """Clears the terminal screen."""
    print("\033[H\033[J", end="")

def loading_bar():
    clear_terminal()
    
    typewriter("Loading . . . \n")
    time.sleep(0.5)

    # 10%
    clear_terminal()
    typewriter(f"{GREEN}-{RED}--------- 10%{RESET}")
    time.sleep(0.2)
    
    # 30%
    clear_terminal()
    typewriter(f"{GREEN}---{RED}------- 30%{RESET}")
    time.sleep(0.7)
    
    # 60%
    clear_terminal()
    typewriter(f"{GREEN}------{RED}---- 60%{RESET}")
    time.sleep(0.4)
    
    # 80%
    clear_terminal()
    typewriter(f"{GREEN}--------{RED}-- 80%{RESET}")
    time.sleep(0.8)
    
    # 90%
    clear_terminal()
    typewriter(f"{GREEN}---------{RED}- 90%{RESET}")
    time.sleep(0.3)
    
    # 99%
    clear_terminal()
    typewriter(f"{GREEN}---------{RED}- 99%{RESET}")
    time.sleep(1.5)
    
    # 100%
    clear_terminal()
    typewriter(f"{GREEN}---------- 100%{RESET}\n")
    time.sleep(1.0)
    
    # Opening
    clear_terminal()
    typewriter(f"{GREEN}OPENING!{RESET}\n")
    time.sleep(0.7)
    clear_terminal()
