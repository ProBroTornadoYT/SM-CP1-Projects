# SM Idiot-proof Assignment

while True:
    try:
        first_name = input("What is your first name: ").strip().title()
        if not first_name.isalpha():
            print("Name cannot be numbers. Please enter a valid name.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid word for first name.")

while True:
    try:
        last_name = input("What is your last name: ").strip().title()
        if not last_name.isalpha():
            print("Name cannot be numbers. Please enter a valid name.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid word for last name.")