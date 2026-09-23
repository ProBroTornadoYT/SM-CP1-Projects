# Color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

# Example usage
print(f"{RED}This text is red!{RESET}")
print(f"{GREEN}This text is green!{RESET}")
print(f"Normal text, {YELLOW}yellow text{RESET}, normal text.")

"""
TERMINAL_EFFECTS_NOTES.PY
A comprehensive reference guide for terminal styling using ANSI escape codes,
24-bit Truecolor RGB, and custom dynamic text loops in Python.
"""

import sys
import time

# ==============================================================================
# 1. CORE ANSI ESCAPE CODE CONSTANTS
# ==============================================================================
# Syntax structure: \033[ STYLE ; FOREGROUND ; BACKGROUND m
RESET = "\033[0m"

# Text Styles
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"       # Note: Highly inconsistent native terminal support
INVERT = "\033[7m"
STRIKE = "\033[9m"

# Standard 16-Color Palette (Foreground Examples)
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# Standard Background Color Examples
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_DARK_GRAY = "\033[100m"


# ==============================================================================
# 2. STATIC TERMINAL EFFECTS EXAMPLES
# ==============================================================================
print("--- 1. STATIC STYLES & MODIFIERS ---")

# Mixing bold + color + reset
print(f"{BOLD}{RED}CRITICAL:{RESET} This is a bold red alert message.")

# Multi-line or sectioned typography
print(f"{DIM}Secondary Log Info: Subsystem 4 isolated.{RESET}")
print(f"{UNDERLINE}Documentation Link:{RESET} https://example.com")
print(f"{STRIKE}Old price: $99.99{RESET} New Price: $49.99")
print(f"{INVERT} INVERTED TEXT (Swaps foreground and background) {RESET}\n")


# ==============================================================================
# 3. 24-BIT RGB TRUECOLOR CUSTOM COLORS
# ==============================================================================
print("--- 2. TRUECOLOR (24-BIT RGB) FORMULAS ---")
# Text RGB Formula:       \033[38;2;R;G;Bm
# Background RGB Formula: \033[48;2;R;G;Bm

neon_pink = "\033[38;2;255;20;147m"
deep_teal_bg = "\033[48;2;0;128;128m"

print(f"{neon_pink}{deep_teal_bg} Neon Pink Text on a Deep Teal Background {RESET}\n")


# ==============================================================================
# 4. DYNAMIC TEXT LOOPS & ANIMATIONS
# ==============================================================================
print("--- 3. DYNAMIC TEXT ANIMATION FUNCTIONS ---")

def matrix_rainbow_typewriter(text: str, delay: float = 0.04) -> None:
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


def smoothly_simulated_blink(text: str, loop_count: int = 4) -> None:
    """Guaranteed cross-platform blinking text using carriage returns (\r)."""
    print(f"{BOLD}Initializing Simulated Hardware Alert Loop...{RESET}")
    
    for _ in range(loop_count):
        # Write text and remain on the same line string block
        sys.stdout.write(f"\r{BOLD}{RED}⚠️ ALERT: {text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        
        # Completely obscure the line by writing empty spaces over the string length
        sys.stdout.write("\r" + " " * (len(text) + 10))
        sys.stdout.flush()
        time.sleep(0.3)
        
    # Leave final state cleanly visible 
    print(f"\r{BOLD}{RED}⚠️ ALERT: {text}{RESET}")


# Execute programmatic dynamic functions
matrix_rainbow_typewriter("Decryption pipeline processing... Access Granted.")
print()
smoothly_simulated_blink("Unauthorized database intrusion detected!")


# ==============================================================================
# 5. RECOMMENDED THIRD-PARTY REPLACEMENTS
# ==============================================================================
"""
If raw ANSI management scales poorly, leverage the following libraries:

1. 'rich' -> Best for standard scripts (tables, emojis, syntax highlights).
   Installation: pip install rich
   Usage: 
       from rich.console import Console
       console = Console()
       console.print("[bold red]Alert![/bold red] [blink]Processing...[/blink]")

2. 'textual' -> Best for interactive complex Terminal User Interfaces (TUIs).
   Installation: pip install textual
"""
