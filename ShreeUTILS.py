import time
import random



def help():
    print(f"Hello, there lets just give you a list of commands we offer!\nfirst you can call typewriter() now you can have a typewriter animation on your sentence for example typewriter(Your print statement)\nSecondly you can use clear_terminal() which just clears your terminal\nthirdly you can use loading_bar to have a loading bar!\nUPDATE 2: added colors function introduces all the colors and prints them recommend using clear terminal right after in a real code\nWe also added textTOvoice function but it only works on linux terminals!\n and just like how typewriter works we have added rainbow_typewriter try trying it")

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
    # Color codes for the terminal
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"  # Stops the color from bleeding into the rest of the terminal
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

def colors():
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
    
    print(f"{RED}RED {GREEN}GREEN {YELLOW}YELLOW {BLUE}BLUE")
    print(f"{BRIGHT_BLACK}BRIGHT_BLACK {BRIGHT_RED}BRIGHT_RED {BRIGHT_GREEN}BRIGHT_GREEN {BRIGHT_YELLOW}BRIGHT_YELLOW")
    print(f"{BRIGHT_BLUE}BRIGHT_BLUE {BRIGHT_MAGENTA}BRIGHT_MAGENTA {BRIGHT_CYAN}BRIGHT_CYAN {BRIGHT_WHITE}BRIGHT_WHITE")
    print(f"{BROWN}BROWN {MAROON}MAROON {CRIMSON}CRIMSON {CORAL}CORAL {PEACH}PEACH")
    print(f"{OLIVE}OLIVE {LIME_GREEN}LIME_GREEN {FOREST_GREEN}FOREST_GREEN {AQUA}AQUA")
    print(f"{SKY_BLUE}SKY_BLUE {NAVY_BLUE}NAVY_BLUE {INDIGO}INDIGO {VIOLET}VIOLET {PLUM}PLUM {MAGENTA}MAGENTA")
    print(f"{DARK_GRAY}DARK_GRAY")
    print(f"{BOLD}BOLD {DIM}DIM {ITALIC}ITALIC {UNDERLINE}UNDERLINE {INVERT}INVERT {STRIKE}STRIKE{RESET}")



def text_to_voice(text):
    import sys
    import os
    """
    Plays native OS voice shortcut to read the provided text aloud.
    """
    print("Playing native OS voice shortcut...")
    
    # Escape single quotes to prevent terminal command injection / syntax errors
    safe_text = text.replace("'", "'\\''")
    
    if sys.platform == "darwin": # macOS
        os.system(f"say '{safe_text}'")
    elif sys.platform.startswith("linux"): # Linux
        os.system(f"spd-say '{safe_text}'")
    else:
        print("Native command line shortcut not supported on Windows without third-party tools.")

def rainbow_typewriter(text: str, delay: float = 0.04) -> None:
    import sys
    RESET = '\033[0m'
    """Prints text character by character cycling through an RGB color wheel."""
    # Custom 24-bit RGB neon spectrum
    colors = [
        (255, 0, 0),    # Red
        (255, 127, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (139, 0, 255)   # Violet
    ]
    
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        # Construct dynamic 24-bit color string
        color_code = f"\033[1;38;2;{r};{g};{b}m"
        
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
        
    print(RESET) # Always cleanly exit formatting at line-end