import turtle
import random
import time

# --- SCREEN SETUP ---
win = turtle.Screen()
win.title("Tag Chase Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0) # Turns off auto-render for smoother performance

# --- GAME VARIABLES ---
score = 0
game_over = False

# --- PLAYER (BLUE) ---
player = turtle.Turtle()
player.shape("turtle")
player.color("cyan")
player.penup()
player.speed(0)
player.goto(0, -200)
player_speed = 15

# --- ENEMY BOT (RED) ---
enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("red")
enemy.penup()
enemy.speed(0)
enemy.goto(0, 200)
enemy_speed = 2.5 # Increase this number to make the game harder!

# --- COIN (GREEN) ---
coin = turtle.Turtle()
coin.shape("circle")
coin.color("lime")
coin.penup()
coin.speed(0)
coin.goto(random.randint(-280, 280), random.randint(-280, 280))

# --- SCORE DISPLAY ---
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# --- MOVEMENT FUNCTIONS ---
def move_up():
    if not game_over and player.ycor() < 280:
        player.setheading(90)
        player.forward(player_speed)

def move_down():
    if not game_over and player.ycor() > -280:
        player.setheading(270)
        player.forward(player_speed)

def move_left():
    if not game_over and player.xcor() > -280:
        player.setheading(180)
        player.forward(player_speed)

def move_right():
    if not game_over and player.xcor() < 280:
        player.setheading(0)
        player.forward(player_speed)

# --- KEYBOARD BINDINGS ---
win.listen()
win.onkeypress(move_up, "Up")
win.onkeypress(move_down, "Down")
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")

# --- MAIN GAME LOOP ---
while not game_over:
    win.update() # Refresh the screen
    time.sleep(0.02) # Cap the framerate

    # Enemy AI: Point towards the player and crawl forward
    enemy.setheading(enemy.towards(player))
    enemy.forward(enemy_speed)

    # Collision Detection: Player touches Coin
    if player.distance(coin) < 20:
        # Move coin to a new random spot
        coin.goto(random.randint(-270, 270), random.randint(-270, 270))
        # Update score
        score += 10
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))
        # Slightly increase enemy speed every time you score to amp up the tension
        enemy_speed += 0.2 

    # Collision Detection: Enemy catches Player (Game Over)
    if player.distance(enemy) < 20:
        game_over = True
        player.color("orange") # Turn player orange on impact
        
        # Display Game Over text
        go_display = turtle.Turtle()
        go_display.color("red")
        go_display.penup()
        go_display.hideturtle()
        go_display.goto(0, 0)
        go_display.write("GAME OVER\nYou got tagged!", align="center", font=("Arial", 24, "bold"))

# Keep window open after game ends until clicked
win.exitonclick()