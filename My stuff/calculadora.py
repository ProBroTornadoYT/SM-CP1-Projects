import sys                                                                                                            
import time                                                                                                            
import random                                                                                                            
import math                                                                                                            
                                                                                                    
RED = '\033[31m'                                                                                                            
GREEN = '\033[32m'                                                                                                            
YELLOW = '\033[33m'                                                                                                            
BLUE = '\033[34m'                                                                                                            
RESET = '\033[0m'                                                                                                            
                                                                                                    
def clear_terminal():                                                                                                            
    print("\033[H\033[J", end="")                                                                                                            
                                                                                                    
clear_terminal()                                                                                                            
                                                                                                    
speed = random.uniform(0.05,0.06)                                                                                                            
                                                                                                    
def typewriter(text: str, delay: float = (speed)) -> None:                                                                                                            
                                                                                                    
    for char in text:                                                                                                            
        sys.stdout.write(char)                                                                                                            
        sys.stdout.flush()                                                                                                            
        time.sleep(delay)                                                                                                            
                                                                                                    
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
                                                                                                    
                                                                                                    
                                                                                                    
print("Calculator")                                                                                                            
                                                                                                    
numbers = []                                                                                                            
                                                                                                    
while True:                                                                                                            
    user_input = input("choose the number or type end: ")                                                                                                            
                                                                                                        
    if user_input == "end":                                                                                                            
        break                                                                                                            
                                                                                                            
    else:                                                                                                            
        try:                                                                                                            
            converted_number = float(user_input)                                                                                                            
            numbers.append(converted_number)                                                                                                            
        except ValueError:                                                                                                            
            print(f"{RED}Invalid input! Please enter a valid number or 'end'.{RESET}")                                                                                                            
                                                                                                    
print("Your numbers are:", numbers)                                                                                                            
                                                                                                    
math_choice = input("Choose what you want to do with the numbers (add,substract,multiply,division): ")                                                                                                            
                                                                                                    
if math_choice == 'add':                                                                                                            
    addition = sum(numbers)                                                                                                            
    print (addition)                                                                                                            
                                                                                                    
if math_choice == 'substract':                                                                                                            
    result = numbers[0]                                                                                                            
                                                                                                    
    for num in numbers[1:]:                                                                                                            
        result = result - num                                                                                                            
                                                                                                            
    print(result)                                                                                                            
                                                                                                    
if math_choice == 'multiply':                                                                                                            
    multiplication = math.prod(numbers)                                                                                                            
    print(multiplication)                                                                                                            
                                                                                                    
if math_choice == 'division':                                                                                                            
                                                                                                    
    divresult = numbers[0]                                                                                                            
                                                                                                        
    for num in numbers[1:]:                                                                                                            
        if num == 0:                                                                                                            
            print("Undefined")                                                                                                            
            break                                                                                                            
        divresult = divresult / num                                                                                                            
    else:                                                                                                            
        print(divresult)                                                                                                            

