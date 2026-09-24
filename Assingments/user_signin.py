# SM 1 User signin and password

import random
import string

def get_username():
    username = input("Type your username: ").lower().strip()
    print(f"Your username has been conveted to lower case for easy use next time: {username}")
    return username

def get_password():
    """Get password - either randomly generated or user-provided."""
    choice = input("Would you like a random password? (1=yes, 2=no): ").strip()
    
    if choice == "1":
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        print(f"Your random password is: {password}")
    else:
        password = input("Enter your password: ").strip()
        print(f"Your password is: {password}")
    
    return password

# Main
username = get_username()
password = get_password()