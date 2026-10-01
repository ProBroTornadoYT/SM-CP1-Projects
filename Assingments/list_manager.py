#SM Shopping list manager

#A Bunch of Color codes for terminal text styling for yk coolness *Enter sigma music*

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
STRIKE = "\033[9m"
BOLD = "\033[1m"

ict = [] #This is the list that will store the items

#asking for their choice

while True:
    print(f"\n {BLUE} ShreeTech {YELLOW}Shopping List Manager!")
    print(f"{GREEN} Type 1 to View list")
    print("Type 2 to Add item")
    print("Type 3 to Remove item")
    print("Type 4 to Exit")
    print("")
    choice = input(f"{GREEN}choose number between 1-4: ")

#For choice 1
    
    if choice == "1":
        if ict:
            print(f"\n {BOLD} Your list: ")
            for i, item in enumerate(ict, 1):
                print(f"{i}. {item}")
        else:
            print("\nYour list is empty")

#For choice 2

    elif choice == "2":
        item = input("Enter item to add: ").strip()
        if item:
            ict.append(item)
            print(f"\n'{item}' added!")
            print("Updated list:", ict)

#For choice 3
    
    elif choice == "3":
        if ict:
            print("\nYour list:", ict)
            try:
                idx = int(input(f"{BOLD} {RED} Enter item number to remove: ")) - 1
                removed = ict.pop(idx)
                print(f"\n'{STRIKE} {removed}' {RESET} {BOLD} {RED} removed!")
                print("Updated list:", ict)
            except (ValueError, IndexError):
                print("Invalid selection")
        else:
            print("\nList is empty")

#For choice 4
    
    elif choice == "4":
        print(f"{BOLD} {YELLOW} Goodbye!")
        break

#IDIOT PROOFING
    
    else:
        print(f"{RED}{BOLD}Invalid choice{RESET}")

