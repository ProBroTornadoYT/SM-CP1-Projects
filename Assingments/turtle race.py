import turtle
import random

# also the black horse in the middle is a logo cuz why not


def setup():
    screen = turtle.Screen()
    screen.setup(700, 500)

    line = turtle.Turtle()
    line.hideturtle()
    line.speed(0)
    line.penup()
    line.goto(280, 200)
    line.pendown()
    line.goto(280, -200)

    # region Describes horse runner i got online

    colors = ["red", "blue", "green", "orange", "purple"]
    y_spots = [-120, -60, 0, 60, 120]
    racers = []

    # I wanted a horse not a turtle so i googled how to do it (not sure if i have to cite the website...)
    horse_coords = (
        (-15, -20), (-15, 0), (-20, 5), (-22, 0), (-20, 10),   # Tail and rear
        (-10, 10), (5, 10), (12, 22), (14, 26), (16, 22),     # Back, neck, and ear
        (22, 18), (20, 14), (13, 14), (12, 0), (14, -20),     # Head and front leg
        (10, -20), (8, -5), (-8, -5), (-10, -20)              # Belly and back leg
    )

    screen.register_shape("horse", horse_coords)

    t = turtle.Turtle()
    t.shape("horse")
    t.tilt(-90)

    # endregion

    # running

    for s in range(5):
        racer = turtle.Turtle()
        racer.shape("horse")
        racer.tilt(-180)
        racer.color(colors[s])
        racer.penup()
        racer.goto(-300, y_spots[s])
        racers.append(racer)

    return racers


def racing(racers):
    for racer in racers:
        racer.forward(random.randint(-5, 10))
        if racer.xcor() >= 280:
            return racer
    return None


def winner(winner, chosen_horse):
    print(winner.pencolor() + " won the day!")
    if chosen_horse == winner.pencolor():
        print("Huzzah! Thy swift and noble steed hath triumphed o'er the field and won the day!")
    else:
        print("Alas! Thy noble steed did fall short of the final mark, and so the crown of victory eluded thee.")


chosen_horse = input("Choose your horse color (red, blue, green, orange, purple): ").lower()
racers = setup()

is_racing = True
while is_racing:
    winner = racing(racers)
    if winner is not None:
        winner(winner, chosen_horse)
        is_racing = False

turtle.done()

