#unit1_final_project.py Shreenayan Mehta

name= input("What is your name: ").strip().title()

job= input("What is your job: ").strip()

address= input("What is your address: ").strip()

email= input("What is your email address: ").strip()

# Password Strentgh Checker

#region Other formatting and stuff
import sys
import time

#new thing i learned
import getpass
#what this does is is that when the user puts in like the password it turns it invisible

#typewriter function
def typewriter(text: str, delay: float = 0.04) -> None:
    """Prints text character by character without color or formatting."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    print()

#another new thing i learned region and endregion
#region Color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
BOLD = "\033[1m"
#endregion


#clear terminal and stuff
def clear_terminal():
    print("\033[H\033[J", end="")

clear_terminal()


#region loading bar

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
#endregion
#endregion

#actual code

password = getpass.getpass("Enter Password: ")

strength = 0

#region defining conditions for seeing that all needed things are there or not
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
#endregion


final_strength = (strength)*13.4

#region final output telling what is rady
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
    typewriter(f"Password Strength is {GREEN}{BOLD}GREAT!{RESET}")
#endregion



print(f"Thank you, {name} Now, your personal details, like your job i.e., {job}. We also know that you live at {address}, and your email address is {email}, and its password is {password}. Now that you have given it to us, let us find some leaks of your information. \nProcessing… \nWe have found one leak on the dark web with these info- \n{name} \n{job} \n{address} \n{email} \n{password}")
