# Multiplication table SM 1 
#Colorful time!
RED = '\033[31m'
YELLOW = '\033[33m'
RESET = '\033[0m'
BOLD = "\033[1m"
print(f"{BOLD}{RED}              MULTIPLICATION TABLE from 1-12{RESET}")
#the top numbers for the multiplication chart
print(f"{YELLOW}   ", end=" ")
for i in range(1, 13):
    print(f"{i:4}", end="")
print()
#the line things for lines like like make square yk
print("   " + "-" * 48)
# MATH TIME
for i in range(1, 13):
    print(f"{i:2} |", end="")
    for j in range(1, 13):
        print(f"{i*j:4}", end="")
    print()




# i did kinda compress the whole code to fit in the least possible lines and look good in the terminal