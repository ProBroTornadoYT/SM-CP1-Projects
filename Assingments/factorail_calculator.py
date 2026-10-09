# SM 1 Factorial Calculator
import math
import sys
import time

#got the ansii code from https://www.ascii-magic.com/text-to-ascii
#got the coloring from personal notes in colored_Text! made using ai so the notes have been made with ai which have utilised here thus that part is not using ai in this code
NAVY_BLUE = '\033[38;5;18m'
AQUA = '\033[38;5;51m'
RESET = '\033[0m'
RED = '\033[31m'
FOREST_GREEN = '\033[38;5;22m'
BRIGHT_RED= '\033[91m'
BOLD = "\033[1m"
BROWN = '\033[38;5;94m'

#"based" on ai made notes
def typewriter(text: str, delay: float = 0.04, end: str = "") -> None:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(end)
    sys.stdout.flush()

#The banner from the website earlier
print(f"""{NAVY_BLUE}{BOLD}
  ____  _                  _____         _         _____          _             _       _      ____      _            _       _                 _   ___  
 / ___|| |__  _ __ ___  __|_   _|__  ___| |__     |  ___|_ _  ___| |_ ___  _ __(_) __ _| |    / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __    / | / _ \ 
 \___ \| '_ \| '__/ _ \/ _ \| |/ _ \/ __| '_ \    | |_ / _` |/ __| __/ _ \| '__| |/ _` | |   | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|   | || | | |
  ___) | | | | | |  __/  __/| |  __/ (__| | | |   |  _| (_| | (__| || (_) | |  | | (_| | |   | |__| (_| | | (__| |_| | | (_| | || (_) | |      | || |_| |
 |____/|_| |_|_|  \___|\___||_|\___|\___|_| |_|   |_|  \__,_|\___|\__\___/|_|  |_|\__,_|_|    \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|      |_(_)___/ 
                                                                                                                                                               
""")
#human made from now on
while True:
    try:
        typewriter(f"{AQUA}Enter the number you want a factorial for {RED} {BOLD} WARNING NUMBERS OVER 1558 WILL BREAK YOUR CODE:{RESET}{FOREST_GREEN} ")
        number = int(input())
    except ValueError:
        typewriter(f"{RESET}{BRIGHT_RED}{BOLD}You need to enter a number not your keyboard spam{RESET}\n")
        continue

    if number < 0:
        typewriter(f"{RESET}{BRIGHT_RED}{BOLD}You need to enter a positive number its just how this works{RESET}\n")
        continue

    if number > 1558:
        typewriter(f"{RESET}{BRIGHT_RED}{BOLD}I am sorry i would have to stop you here THE CODE WILL BREAK for numbers more than 1558 which is a random number but i didnt make the language man and i know you want to do it so just go ahead change the code or sumthing make this message goober fart or something stupid so you user STOP BREAKING MY CODE or i will break the 4th wall and break you alr because the code is unbreakable so that will probably never happen{RESET}\n")
        continue

    break

answer_type = input(f"{BROWN}Quick thing if you want just the direct answer type 1 and if you want the full equation and break your ram by making the computer type 1 x 2 x 3... and so on type 2: ").strip()

if answer_type == '1':
    answer = math.factorial(number)
    typewriter(f"{AQUA}your simplified direct answer is {answer}{RESET}\n")

elif answer_type == '2':
    numbers = list(range(1, number + 1))
    the_thing_that_adds_the_x_thing = " X ".join(map(str, numbers))
    answer = math.factorial(number)
    typewriter(f"{AQUA}{the_thing_that_adds_the_x_thing} = {answer}{RESET}\n")

else:
    typewriter(f"{RESET}{BRIGHT_RED}{BOLD}Choose a number that is 1 or 2 dont put {answer_type}{RESET}\n")