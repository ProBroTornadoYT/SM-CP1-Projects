# Multiplication table SM 1 
#Colorful time!
RED = '\033[31m'         #<- Yes I leanred these ansii color and formatting code
YELLOW = '\033[33m'
RESET = '\033[0m'
BOLD = "\033[1m"
print(f"{BOLD}{RED}              MULTIPLICATION TABLE from 1-12{RESET}")
#the top numbers for the multiplication chart
print(f"{YELLOW}   ", end=" ")#Just makes the whole thing yellow, and the last parrt keeps it on the same line
for i in range(1, 13):#here we write the number at the top and do the i
    print(f"{i:4}", end="")#here the i4 part spaces the numbers 4 aprt from each i number the end make the next code stick together like the opposite of \n 
print()#this is for some white space
#the line things for lines like like make square yk
print("   " + "-" * 48)
#here ^^^ i add^ 3 spaces to keep the thing even
#this is just to have dashes and times by 48 to have 48 dashes
# MATH TIME
for i in range(1, 13): #same thing we did earlier, but here it is vertical down in the base thing and the "|" is used for making striaght lines
    print(f"{i:2} |", end="")
    for j in range(1, 13): #this multiplies the top number with the side number and gives it spaces to line up with the rest
        print(f"{i*j:4}", end="")
    print()   #  ^^^^^ this is the part that does the multiplying and ends the line so no more add and line it up
