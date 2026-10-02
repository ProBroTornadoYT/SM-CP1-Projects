#GAMES!

import random
import sys
import time
from collections import deque
import threading
import select
import os
import msvcrt
import tkinter as tk
from tkinter import messagebox

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"

game = input("Type 1 for truth or dare, Type 2 for love tester, Type 3 for number guessing, Type 4 for impossible rock paper sccisors, type 5 for a madlib game, type 6 for snake game, type 7 for tic-tac-toe: ")



if game == '1':
    print(f"{RED}{BOLD}TIME FOR TRUTH OR DARE! {RESET}")
    print(f"{DIM}{ITALIC}{YELLOW}LOADING... {RESET} ")

    answer = random.randint(1,2)

    if answer == 1:
            print(f"{RED}{BOLD}DARE! {RESET}")
    if answer == 2:
        print(f"{GREEN} {BOLD}TRUTH! {RESET}")



if game == '2':
    person1 = input("Type your first person: ").strip().title()
    person2 = input("Type your second person person: ").strip().title()

    love = random.randint(70,120) 

    print(f"Looks like {person1} loves {person2} at about {love}% love oooh")

    if love > 100:
        print(f"Oh dayum {love}% love is more than 100! thats a match made in heaven")

    if love == 120:
        print("120 percent!!!!!! thats THE MAX AMOUNT OF LOVE!!!!")



if game == '3':
    number = random.randint(1, 100)
    print("Number guessing game: guess the number in 20 tries. It's between 1 and 100")
    tries = 0
    max_tries = 20
    
    while tries < max_tries:
        guess = int(input("Choose your guess: "))
        tries += 1
        
        if guess > number:
            print("Too big")
        elif guess < number:
            print("TOO LOW!")
        elif guess == number:
            print("YOU GUESSED RIGHT")
            break
        else:
            print("Wrong input")
            continue
        
        print(f"Tries remaining: {max_tries - tries}")
    
    if guess != number:
        print(f"YOU LOSE! The number was {number}")



if game == '4':
    quit_game = False
    while not quit_game:
        play = input("Choose one of these MAKE SURE YOU TYPE EXACTLY ( ROCK PAPER SCISSORS ): ").strip().upper()
        if play == "ROCK":
            print("Computer plays: PAPER \n computer has to say you suck idiot")
        elif play == "PAPER":
            print("Computer plays: SCISSORS \n computer has to say you bad bad bad very bad at game funny funny funny")
        elif play == "SCISSORS":
            print("Computer plays: ROCK \n computer has to say how are you soo bad gng")
        else:
            print("Invalid input. Please type ROCK, PAPER, or SCISSORS.")
            continue
        
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            quit_game = True


if game == '5':
    print(f"{BLUE}{BOLD}WELCOME TO THE MADLIB GAME!{RESET}")
    
    adjective1 = input("Enter an adjective: ").strip()
    noun1 = input("Enter a noun: ").strip()
    verb1 = input("Enter a verb: ").strip()
    adjective2 = input("Enter another adjective: ").strip()
    noun2 = input("Enter another noun: ").strip()
    animal = input("Enter an animal: ").strip()
    verb2 = input("Enter another verb: ").strip()
    
    madlib = f"Once upon a time, a {adjective1} {noun1} decided to {verb1} across the street. Suddenly, a {adjective2} {noun2} jumped out and scared a {animal}! The {animal} started to {verb2} uncontrollably. What a strange day it was!"
    
    print(f"\n{YELLOW}{BOLD}HERE'S YOUR STORY:{RESET}\n{madlib}\n")

#Snake game ai made

if game == '6':
    
    WIDTH, HEIGHT = 20, 10
    SNAKE_CHAR = '●'
    FOOD_CHAR = '○'
    EMPTY_CHAR = ' '
    WALL_CHAR = '█'

    snake = deque([(WIDTH // 2, HEIGHT // 2)])
    food = (WIDTH // 4, HEIGHT // 4)
    direction = (1, 0)
    next_direction = (1, 0)
    score = 0
    game_over = False

    def draw_board():
        print('\033[H\033[J', end='')
        print(f"{BLUE}{BOLD}SNAKE GAME - Score: {score}{RESET}")
        
        # Top border
        print(WALL_CHAR * (WIDTH + 2))
        
        for y in range(HEIGHT):
            row = WALL_CHAR
            for x in range(WIDTH):
                if (x, y) in snake:
                    row += SNAKE_CHAR
                elif (x, y) == food:
                    row += FOOD_CHAR
                else:
                    row += EMPTY_CHAR
            row += WALL_CHAR
            print(row)
        
        # Bottom border
        print(WALL_CHAR * (WIDTH + 2))
        print("Use arrow keys: UP/DOWN/LEFT/RIGHT or W/A/S/D (or Q to quit)")

    def get_input():
        global next_direction, game_over
        
        opposite_directions = {
            (1, 0): (-1, 0),
            (-1, 0): (1, 0),
            (0, 1): (0, -1),
            (0, -1): (0, 1)
        }
        
        if os.name == 'nt':  # Windows
            if msvcrt.kbhit():
                key = msvcrt.getch().decode().upper()
                if key in ['W', 'A', 'S', 'D']:
                    new_dir = None
                    if key == 'W': new_dir = (0, -1)
                    elif key == 'S': new_dir = (0, 1)
                    elif key == 'A': new_dir = (-1, 0)
                    elif key == 'D': new_dir = (1, 0)
                    if new_dir != opposite_directions.get(direction):
                        next_direction = new_dir
                elif key == 'Q':
                    game_over = True
        else:  # Linux/Mac
            try:
                if select.select([sys.stdin], [], [], 0)[0]:
                    key = sys.stdin.read(1).upper()
                    if key in ['W', 'A', 'S', 'D']:
                        new_dir = None
                        if key == 'W': new_dir = (0, -1)
                        elif key == 'S': new_dir = (0, 1)
                        elif key == 'A': new_dir = (-1, 0)
                        elif key == 'D': new_dir = (1, 0)
                        if new_dir != opposite_directions.get(direction):
                            next_direction = new_dir
                    elif key == 'Q':
                        game_over = True
            except:
                pass

    print(f"{BLUE}{BOLD}WELCOME TO SNAKE!{RESET}")
    print("Eat the food (○) to grow. Don't hit walls or yourself!")

    while not game_over:
        draw_board()
        get_input()
        
        direction = next_direction
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])
        
        if (new_head[0] < 0 or new_head[0] >= WIDTH or 
            new_head[1] < 0 or new_head[1] >= HEIGHT or 
            new_head in snake):
            game_over = True
            break
        
        snake.appendleft(new_head)
        
        if new_head == food:
            score += 10
            food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
        else:
            snake.pop()
        
        time.sleep(0.2)

    draw_board()
    print(f"{RED}{BOLD}GAME OVER! Final Score: {score}{RESET}")



if game == '7':
    class TicTacToe:
        def __init__(self, mode):
            self.mode = mode  # "2player" or "computer"
            self.window = tk.Tk()
            self.window.title("Tic-Tac-Toe")
            self.window.geometry("400x450")
            self.board = [''] * 9
            self.human = 'X'
            self.computer = 'O'
            self.current_player = 'X'
            self.buttons = []
            self.game_over = False
            
            self.label = tk.Label(self.window, text="Tic-Tac-Toe", font=("Arial", 20, "bold"))
            self.label.pack(pady=10)
            
            frame = tk.Frame(self.window)
            frame.pack()
            
            for i in range(9):
                btn = tk.Button(frame, text='', font=("Arial", 20), width=6, height=3,
                               command=lambda idx=i: self.on_click(idx))
                btn.grid(row=i//3, column=i%3, padx=2, pady=2)
                self.buttons.append(btn)
            
            self.window.mainloop()
        
        def on_click(self, idx):
            if self.board[idx] == '' and not self.game_over:
                self.board[idx] = self.current_player
                self.buttons[idx].config(text=self.current_player)
                
                if self.check_winner(self.current_player):
                    winner = "You won!" if self.current_player == self.human else "Computer won!"
                    messagebox.showinfo("Game Over", winner)
                    self.game_over = True
                    return
                
                if '' not in self.board:
                    messagebox.showinfo("Game Over", "It's a tie!")
                    self.game_over = True
                    return
                
                if self.mode == "computer":
                    self.computer_move()
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        def computer_move(self):
            best_score = float('-inf')
            best_move = None
            
            for i in range(9):
                if self.board[i] == '':
                    self.board[i] = self.computer
                    score = self.minimax(0, False)
                    self.board[i] = ''
                    
                    if score > best_score:
                        best_score = score
                        best_move = i
            
            if best_move is not None:
                self.board[best_move] = self.computer
                self.buttons[best_move].config(text=self.computer)
                
                if self.check_winner(self.computer):
                    messagebox.showinfo("Game Over", "Computer won!")
                    self.game_over = True
                elif '' not in self.board:
                    messagebox.showinfo("Game Over", "It's a tie!")
                    self.game_over = True
        
        def minimax(self, depth, is_maximizing):
            if self.check_winner(self.computer):
                return 10 - depth
            if self.check_winner(self.human):
                return depth - 10
            if '' not in self.board:
                return 0
            
            if is_maximizing:
                best_score = float('-inf')
                for i in range(9):
                    if self.board[i] == '':
                        self.board[i] = self.computer
                        best_score = max(best_score, self.minimax(depth + 1, False))
                        self.board[i] = ''
                return best_score
            else:
                best_score = float('inf')
                for i in range(9):
                    if self.board[i] == '':
                        self.board[i] = self.human
                        best_score = min(best_score, self.minimax(depth + 1, True))
                        self.board[i] = ''
                return best_score
        
        def check_winner(self, player):
            lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
            return any(all(self.board[i] == player for i in line) for line in lines)

    mode = input("Play against (1) computer or (2) another player? ").strip()
    mode_str = "computer" if mode == '1' else "2player"
    TicTacToe(mode_str)