# SM 1 Factorial Calculator
import math

#got the ansii code from https://www.ascii-magic.com/text-to-ascii
NAVY_BLUE = '\033[38;5;18m'
AQUA = '\033[38;5;51m'
RESET = '\033[0m'
RED = '\033[31m'
FOREST_GREEN = '\033[38;5;22m'
BRIGHT_RED= '\033[91m'
BOLD = "\033[1m"

print(f"""{NAVY_BLUE}{BOLD}
  ____  _                  _____         _         _____          _             _       _      ____      _            _       _                 _   ___  
 / ___|| |__  _ __ ___  __|_   _|__  ___| |__     |  ___|_ _  ___| |_ ___  _ __(_) __ _| |    / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __    / | / _ \ 
 \___ \| '_ \| '__/ _ \/ _ \| |/ _ \/ __| '_ \    | |_ / _` |/ __| __/ _ \| '__| |/ _` | |   | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|   | || | | |
  ___) | | | | | |  __/  __/| |  __/ (__| | | |   |  _| (_| | (__| || (_) | |  | | (_| | |   | |__| (_| | | (__| |_| | | (_| | || (_) | |      | || |_| |
 |____/|_| |_|_|  \___|\___||_|\___|\___|_| |_|   |_|  \__,_|\___|\__\___/|_|  |_|\__,_|_|    \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|      |_(_)___/ 
                                                                                                                                                               
""")

while True:
    try:
        number = int(input(f"{AQUA}Enter the number you want a factorial for:{RESET}{FOREST_GREEN} "))
    except ValueError:
        print(f"{RESET}{BRIGHT_RED}{BOLD}You need to enter a number.{RESET}")
        continue

    if number < 0:
        print(f"{RESET}{BRIGHT_RED}{BOLD}You need to enter a positive number.{RESET}")
        continue
    
    break

numbers = list(range(1, number + 1))
factorials = list(map(math.factorial, numbers))

the_thing_that_does_the_multiply_thing = " x ".join(map(str, numbers))
answer = math.factorial(number)

print(f"{AQUA}{the_thing_that_does_the_multiply_thing} = {answer}")

