# SM 1 User signin and password

import random
import string
import sys
import time

# ANSI color reset code
RESET = "\033[0m"

#Warning this part that makes a list for the users has utilized the use of Artificial Intelligence as a brainstorming tool and not a "writer" as the code has still been written by me.

# area for storing userinfo
users = {}

def get_username():
    username = input("Type your username: ").lower().strip()
    print("Your username has been converted to lower case for easyness of using next time")
    print(f"Your username is {username}")
    return username

def get_password():
    password = input("Would you like a random password? type '1' for yes and '2' for no: ").strip()

#Warning the part on how to generate a random code has utilized the use of Artificial Intelligence as a brainstroming tool and not a "writer" as the code has still been written by me.
    
    if password == "1":
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        print(f"Your random password is: {password}")
    else:
        password = input("Enter your password: ").strip()
    
    return password

#Warning the part that makes the rainbow color loop has utilized the use of Artificial Intelligence as a brainstorming tool and not a "writer" as the code has still been written by me.

def matrix_rainbow_typewriter(text: str, delay: float = 0.04) -> None:
    colors = [
        (255, 0, 0), (255, 127, 0), (255, 255, 0),
        (0, 255, 0), (0, 0, 255), (139, 0, 255)
    ]
    
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        color_code = f"\033[1;38;2;{r};{g};{b}m"
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
    print(RESET)


#the place or the software thing
while True:
    choice = input("\nType '1' to sign up or '2' to log in: ").strip()
    
    if choice == "1":
        print("\n--- SIGN UP ---")
        username = get_username()
        if username in users:
            print("Username already exists!")
            continue
        password = get_password()
        users[username] = password
        matrix_rainbow_typewriter(f"\nAccount created!\nUsername: {username}\n")
        
    elif choice == "2":
        print("\n--- LOG IN ---")
        username = input("Enter your username: ").lower().strip()
        if username not in users:
            print("Username not found. Please sign up first.")
            continue
        
        password = input("Enter your password: ").strip()
        if users[username] == password:
            matrix_rainbow_typewriter("Access Granted.")
            print(f"Logged in as {username}")
            break
        else:
            print("Wrong password try again")
    else:
        print("Invalid input")
