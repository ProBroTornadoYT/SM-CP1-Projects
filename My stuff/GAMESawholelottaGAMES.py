#GAMES!

import random
import sys
import time
import os
from collections import deque
import select

try:
    import msvcrt
except ImportError:  # pragma: no cover - only on non-Windows systems
    msvcrt = None

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:  # pragma: no cover - tkinter may be unavailable in headless envs
    tk = None
    messagebox = None

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

user_name = 'Player'
is_admin = False


def style(text, *codes):
    return ''.join(codes) + text + RESET


def print_banner(title, color=BLUE):
    border = '=' * (len(title) + 12)
    print(style(border, BOLD, color))
    print(style(f"  {title}", BOLD, color))
    print(style(border, BOLD, color))


def print_prompt(text):
    text = f'{user_name}, {text}'
    return input(style(text, CYAN, BOLD))


def run_game_hub():
    global user_name, is_admin
    user_name = input(style('What is your username? ', CYAN, BOLD)).strip() or 'Player'
    is_admin = user_name == 'Shree67'

    while True:
        print_banner('WELCOME TO THE GAME HUB', MAGENTA)
        print(style(f'Welcome, {user_name}! Pick a game and let the fun begin!', WHITE, BOLD))
        if is_admin:
            print(style('ADMIN ACCESS: game 14 opens the admin console; type "admin" in number guessing to reveal the answer.', GREEN, BOLD))

        game = os.environ.pop('GAME_HUB_SELECTION', None)
        if game is None:
            choices = "Choose 1 truth or dare, 2 love tester, 3 number guessing, 4 rock paper scissors, 5 madlib, 6 snake, 7 tic-tac-toe, 8 hangman, 9 pong, 10 flappy bird, 11 space invaders, 12 minesweeper, 13 space colony"
            if is_admin:
                choices += ', 14 admin console'
            game = print_prompt(choices + ': ').strip()

        if game == '14' and is_admin:
            print_banner('ADMIN CONSOLE', GREEN)
            print(style(f'Welcome, Administrator {user_name}. The admin console grants bonus colony resources.', GREEN, BOLD))
            game = print_prompt('Choose a game to launch (1-13): ').strip()

        if game == '1':
            print_banner('TRUTH OR DARE', RED)
            print(style('LOADING...', DIM, ITALIC, YELLOW))

            answer = random.randint(1, 2)

            if answer == 1:
                print(style('DARE!', RED, BOLD))
            else:
                print(style('TRUTH!', GREEN, BOLD))

        elif game == '2':
            person1 = print_prompt("Type your first person: ").strip().title()
            person2 = print_prompt("Type your second person: ").strip().title()

            love = random.randint(70, 120)

            print(style(f"{user_name}, looks like {person1} loves {person2} at about {love}% love oooh", CYAN, BOLD))

            if love > 100:
                print(style(f"Oh dayum {love}% love is more than 100! that's a match made in heaven", GREEN, BOLD))

            if love == 120:
                print(style("120 percent!!!!!! that's THE MAX AMOUNT OF LOVE!!!!", YELLOW, BOLD))

        elif game == '3':
            number = random.randint(1, 100)
            print_banner('NUMBER GUESSING', BLUE)
            print(style("Guess the number in 20 tries. It's between 1 and 100.", WHITE, BOLD))
            tries = 0
            max_tries = 20
            guess = None

            while tries < max_tries:
                try:
                    guess_text = print_prompt("Choose your guess: ").strip()
                    if is_admin and guess_text.lower() == 'admin':
                        print(style(f'Admin reveal: the number is {number}.', MAGENTA, BOLD))
                        continue
                    guess = int(guess_text)
                except ValueError:
                    print(style('Please enter a valid number!', RED, BOLD))
                    continue

                tries += 1

                if guess > number:
                    print(style('Too big!', YELLOW, BOLD))
                elif guess < number:
                    print(style('TOO LOW!', YELLOW, BOLD))
                elif guess == number:
                    print(style(f'{user_name}, you guessed right!', GREEN, BOLD))
                    break
                else:
                    print(style('Wrong input', RED, BOLD))
                    continue

                print(style(f"Tries remaining: {max_tries - tries}", CYAN, BOLD))

            if guess != number:
                print(style(f"YOU LOSE! The number was {number}", RED, BOLD))

        elif game == '4':
            print_banner('IMPOSSIBLE ROCK PAPER SCISSORS', YELLOW)
            quit_game = False
            while not quit_game:
                play = print_prompt("Choose one of these MAKE SURE YOU TYPE EXACTLY ( ROCK PAPER SCISSORS ): ").strip().upper()
                if play == "ROCK":
                    print(style("Computer plays: PAPER\nComputer says: YOU SUCK IDIOT!", RED, BOLD))
                elif play == "PAPER":
                    print(style("Computer plays: SCISSORS\nComputer says: YOU BAD BAD BAD VERY BAD AT GAME!", RED, BOLD))
                elif play == "SCISSORS":
                    print(style("Computer plays: ROCK\nComputer says: HOW ARE YOU SO BAD GNG", RED, BOLD))
                else:
                    print(style("Invalid input. Please type ROCK, PAPER, or SCISSORS.", RED, BOLD))
                    continue

                play_again = print_prompt("Play again? (yes/no): ").strip().lower()
                if play_again != "yes":
                    quit_game = True

        elif game == '5':
            print_banner('MADLIB GAME', BLUE)

            adjective1 = print_prompt("Enter an adjective: ").strip()
            noun1 = print_prompt("Enter a noun: ").strip()
            verb1 = print_prompt("Enter a verb: ").strip()
            adjective2 = print_prompt("Enter another adjective: ").strip()
            noun2 = print_prompt("Enter another noun: ").strip()
            animal = print_prompt("Enter an animal: ").strip()
            verb2 = print_prompt("Enter another verb: ").strip()

            madlib = (
                f"Once upon a time, a {adjective1} {noun1} decided to {verb1} across the street. "
                f"Suddenly, a {adjective2} {noun2} jumped out and scared a {animal}! The {animal} started to {verb2} "
                f"uncontrollably. What a strange day it was!"
            )

            print(style('\nHERE\'S YOUR STORY:\n', YELLOW, BOLD))
            print(style(madlib, WHITE, BOLD))

        elif game == '6':
            print_banner('SNAKE GAME', GREEN)
            print(style("Eat the food (○) to grow. Don't hit walls or yourself!", WHITE, BOLD))

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
                print(style(f'SNAKE GAME - Score: {score}', BLUE, BOLD))
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

                print(WALL_CHAR * (WIDTH + 2))
                print(style('Use arrow keys: UP/DOWN/LEFT/RIGHT or W/A/S/D (or Q to quit)', CYAN, BOLD))

            def get_input():
                nonlocal direction, next_direction, game_over

                opposite_directions = {
                    (1, 0): (-1, 0),
                    (-1, 0): (1, 0),
                    (0, 1): (0, -1),
                    (0, -1): (0, 1)
                }

                keys = []

                if sys.platform.startswith('win') and msvcrt is not None:
                    if msvcrt.kbhit():
                        keys.append(msvcrt.getch().decode().upper())
                elif hasattr(select, 'select'):
                    try:
                        if select.select([sys.stdin], [], [], 0)[0]:
                            keys.append(sys.stdin.read(1).upper())
                    except (OSError, ValueError):
                        pass

                for key in keys:
                    if key in ['W', 'A', 'S', 'D']:
                        new_dir = None
                        if key == 'W':
                            new_dir = (0, -1)
                        elif key == 'S':
                            new_dir = (0, 1)
                        elif key == 'A':
                            new_dir = (-1, 0)
                        elif key == 'D':
                            new_dir = (1, 0)

                        if new_dir is not None and new_dir != opposite_directions.get(direction):
                            next_direction = new_dir
                    elif key == 'Q':
                        game_over = True

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
            print(style(f'GAME OVER! Final Score: {score}', RED, BOLD))

        elif game == '7':
            if tk is None or messagebox is None:
                print(style('Tkinter is not available in this environment, so Tic-Tac-Toe cannot run here.', RED, BOLD))
            else:
                class TicTacToe:
                    def __init__(self, mode):
                        self.mode = mode
                        self.window = tk.Tk()
                        self.window.title('Tic-Tac-Toe')
                        self.window.geometry('400x450')
                        self.board = [''] * 9
                        self.human = 'X'
                        self.computer = 'O'
                        self.current_player = 'X'
                        self.buttons = []
                        self.game_over = False

                        self.label = tk.Label(self.window, text='Tic-Tac-Toe', font=('Arial', 20, 'bold'))
                        self.label.pack(pady=10)

                        frame = tk.Frame(self.window)
                        frame.pack()

                        for i in range(9):
                            btn = tk.Button(frame, text='', font=('Arial', 20), width=6, height=3,
                                           command=lambda idx=i: self.on_click(idx))
                            btn.grid(row=i // 3, column=i % 3, padx=2, pady=2)
                            self.buttons.append(btn)

                        self.window.mainloop()

                    def on_click(self, idx):
                        if self.board[idx] == '' and not self.game_over:
                            self.board[idx] = self.current_player
                            self.buttons[idx].config(text=self.current_player)

                            if self.check_winner(self.current_player):
                                winner = 'You won!' if self.current_player == self.human else 'Computer won!'
                                messagebox.showinfo('Game Over', winner)
                                self.game_over = True
                                return

                            if '' not in self.board:
                                messagebox.showinfo('Game Over', "It's a tie!")
                                self.game_over = True
                                return

                            if self.mode == 'computer':
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
                                messagebox.showinfo('Game Over', 'Computer won!')
                                self.game_over = True
                            elif '' not in self.board:
                                messagebox.showinfo('Game Over', "It's a tie!")
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
                        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
                        return any(all(self.board[i] == player for i in line) for line in lines)

                mode = print_prompt("Play against (1) computer or (2) another player? ").strip()
                mode_str = 'computer' if mode == '1' else '2player'
                TicTacToe(mode_str)

        elif game == '8':
            print_banner('HANGMAN', YELLOW)
            words = ['planet', 'galaxy', 'computer', 'python', 'colony', 'asteroid', 'rocket']
            word = random.choice(words)
            guessed = set()
            wrong = set()
            lives = 6
            while lives and not set(word).issubset(guessed):
                shown = ' '.join(letter if letter in guessed else '_' for letter in word)
                print(style(f'Word: {shown}   Wrong guesses: {", ".join(sorted(wrong)) or "none"}   Lives: {lives}', CYAN, BOLD))
                guess = print_prompt('Guess a letter: ').strip().lower()
                if len(guess) != 1 or not guess.isalpha():
                    print(style('Enter one letter.', RED, BOLD))
                elif guess in guessed or guess in wrong:
                    print(style('You already guessed that letter.', YELLOW, BOLD))
                elif guess in word:
                    guessed.add(guess)
                else:
                    wrong.add(guess)
                    lives -= 1
            if set(word).issubset(guessed):
                print(style(f'You win! The word was {word}.', GREEN, BOLD))
            else:
                print(style(f'Out of lives! The word was {word}.', RED, BOLD))

        elif game == '9':
            print_banner('PONG', CYAN)
            print(style('Move your paddle with W (up), S (down), or Enter (stay). First to 5 wins.', WHITE, BOLD))
            height, ball_y, ball_x, dy, dx = 9, 4, 4, random.choice([-1, 1]), 1
            player, computer = 0, 0
            while player < 5 and computer < 5:
                move = print_prompt('Your move [W/S/Enter]: ').strip().lower()
                paddle = max(1, min(height - 2, (height // 2) + (move == 's') - (move == 'w')))
                ball_x += dx
                ball_y += dy
                if ball_y <= 0 or ball_y >= height - 1:
                    dy *= -1
                    ball_y += 2 * dy
                computer_paddle = max(1, min(height - 2, ball_y if random.random() < 0.7 else (height // 2)))
                if ball_x >= 8:
                    dx = -1
                elif ball_x <= 1:
                    if abs(ball_y - paddle) <= 1:
                        dx = 1
                    else:
                        computer += 1
                        ball_x, ball_y, dx, dy = 4, 4, 1, random.choice([-1, 1])
                if ball_x >= 8 and abs(ball_y - computer_paddle) > 1:
                    player += 1
                    ball_x, ball_y, dx, dy = 4, 4, -1, random.choice([-1, 1])
                print(style(f'Score You {player} - {computer} Computer', YELLOW, BOLD))
                for y in range(height):
                    left = '|' if abs(y - paddle) <= 1 else ' '
                    right = '|' if abs(y - computer_paddle) <= 1 else ' '
                    print(left + ''.join('o' if (x, y) == (ball_x, ball_y) else ' ' for x in range(1, 9)) + right)
            print(style('You win!' if player == 5 else 'Computer wins!', GREEN if player == 5 else RED, BOLD))

        elif game == '10':
            print_banner('FLAPPY BIRD', YELLOW)
            height, bird, velocity, pipe_x = 8, 4, 0, 10
            gap = random.randint(2, 5)
            score = 0
            while 0 <= bird < height:
                print(style(f'Height {bird} | Pipe distance {pipe_x} | Score {score}', CYAN, BOLD))
                print(''.join('B' if y == bird else '|' if pipe_x <= 0 and y not in (gap, gap + 1) else '.' for y in range(height)))
                if print_prompt('Press Enter to flap, or type q to quit: ').strip().lower() == 'q':
                    break
                velocity = -2 if velocity > 1 else velocity + 1
                bird += velocity
                pipe_x -= 1
                if pipe_x < 0:
                    if bird not in (gap, gap + 1):
                        break
                    score += 1
                    pipe_x, gap = 10, random.randint(2, 5)
            print(style(f'Game over! Score: {score}', GREEN if bird in range(height) else RED, BOLD))

        elif game == '11':
            print_banner('SPACE INVADERS', MAGENTA)
            width = 10
            aliens = {(x, y) for y in range(2) for x in range(2, 8)}
            ship = width // 2
            while aliens:
                print(style(f"Aliens remaining: {len(aliens)}", CYAN, BOLD))
                for y in range(5):
                    print(''.join('A' if (x, y) in aliens else '^' if y == 4 and x == ship else '.' for x in range(width)))
                action = print_prompt('Move A/D, then press Enter to fire (Q quits): ').strip().lower()
                if action == 'q':
                    break
                if 'a' in action:
                    ship = max(0, ship - 1)
                if 'd' in action:
                    ship = min(width - 1, ship + 1)
                targets = sorted((x, y) for x, y in aliens if x == ship)
                if targets:
                    aliens.remove(targets[-1])
                elif aliens:
                    aliens = {(x, y + 1) for x, y in aliens}
                    if any(y >= 4 for _, y in aliens):
                        break
            print(style('You cleared the invasion!' if not aliens else 'The invaders reached your ship!', GREEN if not aliens else RED, BOLD))

        elif game == '12':
            print_banner('MINESWEEPER', BLUE)
            size, mine_count = 8, 10
            mines = set(random.sample(range(size * size), mine_count))
            revealed, flagged = set(), set()
            def mine_neighbors(cell):
                x, y = cell % size, cell // size
                return [ny * size + nx for ny in range(max(0, y - 1), min(size, y + 2))
                        for nx in range(max(0, x - 1), min(size, x + 2)) if (nx, ny) != (x, y)]
            def show_mines_board(show_all=False):
                print('   ' + ' '.join(str(x) for x in range(size)))
                for y in range(size):
                    row = []
                    for x in range(size):
                        cell = y * size + x
                        if cell in flagged:
                            row.append('F')
                        elif cell in revealed or show_all:
                            row.append('*' if cell in mines else str(sum(n in mines for n in mine_neighbors(cell))) if any(n in mines for n in mine_neighbors(cell)) else '.')
                        else:
                            row.append('#')
                    print(f'{y:2} ' + ' '.join(row))
            lost = False
            while len(revealed) < size * size - mine_count:
                show_mines_board()
                command = print_prompt('Enter row col to reveal, or f row col to flag: ').strip().split()
                try:
                    if len(command) == 3 and command[0].lower() == 'f':
                        cell = int(command[1]) * size + int(command[2])
                        if not (0 <= int(command[1]) < size and 0 <= int(command[2]) < size):
                            raise ValueError
                        flagged.symmetric_difference_update({cell})
                        continue
                    if len(command) != 2:
                        raise ValueError
                    y, x = map(int, command)
                    if not (0 <= x < size and 0 <= y < size):
                        raise ValueError
                    cell = y * size + x
                except ValueError:
                    print(style('Enter valid coordinates from 0 to 7.', RED, BOLD))
                    continue
                if cell in flagged or cell in revealed:
                    continue
                if cell in mines:
                    lost = True
                    break
                pending = [cell]
                while pending:
                    current = pending.pop()
                    if current in revealed or current in mines:
                        continue
                    revealed.add(current)
                    neighbors = mine_neighbors(current)
                    if not any(n in mines for n in neighbors):
                        pending.extend(n for n in neighbors if n not in revealed)
            show_mines_board(show_all=lost)
            print(style('Boom! Game over.' if lost else 'You cleared the minefield!', RED if lost else GREEN, BOLD))

        elif game == '13':
            print_banner('SPACE FLEET & COLONY MANAGER', GREEN)
            minerals, energy, crew, credits = 100, 100, 30, 100
            solar, turrets, day = 1, 0, 1
            while crew > 0:
                print(style(f'Day {day} | Minerals {minerals} | Energy {energy} | Crew {crew} | Credits {credits} | Solar {solar} | Turrets {turrets}', CYAN, BOLD))
                event = random.choice(['quiet', 'flare', 'meteor', 'trade'])
                if event == 'flare':
                    print(style('Solar flare! Your energy grid is disrupted. Ration power: drills lose 50 minerals (if available), or life support costs 5 crew.', YELLOW, BOLD))
                    choice = print_prompt('Choose drills or life support: ').strip().lower()
                    if choice == 'life support':
                        crew -= 5
                    else:
                        minerals = max(0, minerals - 50)
                elif event == 'meteor':
                    print(style('Meteor debris is approaching! Your turrets intercept some, but repairs cost 15 minerals.', YELLOW, BOLD))
                    minerals = max(0, minerals - 15)
                elif event == 'trade':
                    print(style('A passing freighter offers a mineral shipment for 20 credits.', YELLOW, BOLD))
                    if print_prompt('Buy it? (yes/no): ').strip().lower() in ('yes', 'y') and credits >= 20:
                        credits -= 20
                        minerals += 30
                energy = max(0, energy - 10)
                crew = max(0, crew - (2 if energy == 0 else 1))
                credits += max(1, solar)
                while True:
                    print('1) Upgrade solar array (30 minerals, 20 credits)  2) Mining expedition (5 crew)')
                    print('3) Buy turret (25 minerals, 30 credits)  4) End day  5) Quit')
                    if is_admin:
                        print('6) Admin resource grant (+100 minerals, energy, credits; +10 crew)')
                    action = print_prompt('Colony action: ').strip()
                    if action == '1' and minerals >= 30 and credits >= 20:
                        minerals -= 30
                        credits -= 20
                        solar += 1
                        energy += 20
                    elif action == '2' and crew >= 5:
                        crew -= 5
                        minerals += random.randint(20, 45)
                        credits += random.randint(5, 20)
                        print(style('The expedition returned with resources.', GREEN, BOLD))
                    elif action == '3' and minerals >= 25 and credits >= 30:
                        minerals -= 25
                        credits -= 30
                        turrets += 1
                    elif action == '4':
                        break
                    elif action == '5':
                        crew = 0
                        break
                    elif action == '6' and is_admin:
                        minerals += 100
                        energy = min(100, energy + 100)
                        crew += 10
                        credits += 100
                        print(style('Admin resource grant applied.', GREEN, BOLD))
                    else:
                        print(style('Not enough resources or invalid action.', RED, BOLD))
                energy = min(100, energy + solar * 10)
                if crew > 0:
                    day += 1
            print(style(f'Colony report: survived {day - 1} days, built {solar - 1} solar upgrades and {turrets} turrets.', GREEN, BOLD))

        elif game == '14' and not is_admin:
            print(style('Invalid game selection. Please choose 1 through 13.', RED, BOLD))
            return

        else:
            print(style('Invalid game selection. Please choose 1 through 13.', RED, BOLD))
            return

        play_again = print_prompt('Play this game again? (yes/no): ').strip().lower()
        if play_again in ('yes', 'y'):
            next_game = game
        else:
            next_game = print_prompt('Choose your next game (1-13), or Q to quit: ').strip().lower()
            if next_game == 'q':
                print(style('Thanks for playing!', WHITE, BOLD))
                return

        if next_game not in {str(number) for number in range(1, 14)}:
            print(style('Invalid game selection. Please choose 1 through 13.', RED, BOLD))
            return

        os.environ['GAME_HUB_SELECTION'] = next_game


if __name__ == "__main__":
    run_game_hub()

