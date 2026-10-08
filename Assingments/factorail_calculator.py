def thing():
    while True:
        try:
            number = int(input("ENTER A NUMBER: "))
        except ValueError:
            print("uh you need to put in a number homie")
            continue

        if number < 0:
            print("also you need to put a positive number mb homie")
            continue

        factorial = 1
        values = []

        for value in range(1, number + 1):
            values.append(value)
            factorial *= value

        if number == 0:
            print(f"{number}! = 1")
            continue

        print(f"{number}! = {' + '.join(str(value) for value in values)} = {factorial}")


if __name__ == "__main__":
    thing()
