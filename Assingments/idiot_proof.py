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

while True:
    try:
        phone_number = input("What is your phone number: ").strip()
        if not phone_number.isdigit():
            print("Phone number must be a number. Please enter a valid phone number.")
            continue
        if len(phone_number) != 10:
            raise Exception("Phone number must be 10 digits long. Please enter a valid phone number. Try again")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for phone number.")
        
        break
    except ValueError:
        print("Invalid input. Please enter a valid number for phone number.")

while True:
    try:
        gpa = input("What is your gpa: ").strip()
        if not gpa.replace('.', '', 1).isdigit():
            print("GPA must be a number. Please enter a valid GPA.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid GPA.")

print(f"Hello {first_name} {last_name}, your phone number is {phone_number} and your GPA is {gpa}.")

if float(gpa) >= 3.5:
    print("good You have a good GPA.")
else:
    print("WHAT THE HECKS THAT GPA BROTHER EVEN A TODDLER HAS A BETTER GPA THAN THAT. (Imagine getting cooked by a computer)")

if first_name == "Admin":
    print("Welcome, admin! You have special privileges.")
    print("which are none")

if phone_number.startswith("6767676767"):
    print("GET OUT KID GO GIVE THE PHONE TO YOUR MOM STAY OFF THE IPAD")

