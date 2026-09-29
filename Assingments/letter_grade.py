#SM Letter grade assignment 1

print("Your grade calculator")

print("")
while True:
    try:
        grade1 = float(input("Type your grade: "))
        if 0 <= grade1 <= 100:
            break
        else:
            print("Please enter a grade between 0 and 100")
    except ValueError:
        print("Invalid Input")

if grade1 >= 93:
    print (f"You have gotten {grade1}% which means a A")
elif grade1 >= 90:
    print(f"You have gotten {grade1}% which means a A-")
elif grade1 >= 87:
    print(f"You have gotten {grade1}% which means a B+")
elif grade1 >= 83:
    print(f"You have gotten {grade1}% which means a B")
elif grade1 >= 80:
    print(f"You have gotten {grade1}% which means a B-")
elif grade1 >= 77:
    print(f"You have gotten {grade1}% which means a C+")
elif grade1 >= 73:
    print(f"You have gotten {grade1}% which means a C")
elif grade1 >= 70:
    print(f"You have gotten {grade1}% which means a C-")
elif grade1 >= 67:
    print(f"You have gotten {grade1}% which means a D+")
elif grade1 >= 63:
    print(f"You have gotten {grade1}% which means a D")
elif grade1 >= 60:
    print(f"You have gotten {grade1}% which means a D-")
else:
    print(f"You have gotten {grade1}% which means a F")

