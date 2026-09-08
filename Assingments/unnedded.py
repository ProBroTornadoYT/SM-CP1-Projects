while True:
    try:
        # Your code here
        user_input = input("Enter something: ")
        result = int(user_input)
        print(f"You entered: {result}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nExiting...")
        break