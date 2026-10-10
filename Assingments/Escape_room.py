#SM 1 Escape room

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
BRIGHT_BLACK= '\033[90m'
BRIGHT_RED= '\033[91m'
BRIGHT_GREEN= '\033[92m'
BRIGHT_YELLOW= '\033[93m'
BRIGHT_BLUE= '\033[94m'
BRIGHT_MAGENTA= '\033[95m'
BRIGHT_CYAN= '\033[96m'
BRIGHT_WHITE= '\033[97m'
BROWN = '\033[38;5;94m'
MAROON = '\033[38;5;88m'
CRIMSON = '\033[38;5;160m'
CORAL = '\033[38;5;209m'
PEACH = '\033[38;5;216m'
OLIVE = '\033[38;5;100m'
LIME_GREEN = '\033[38;5;46m'
FOREST_GREEN = '\033[38;5;22m'
AQUA = '\033[38;5;51m'
SKY_BLUE = '\033[38;5;117m'
NAVY_BLUE = '\033[38;5;18m'
INDIGO = '\033[38;5;54m'
VIOLET = '\033[38;5;129m'
PLUM = '\033[38;5;96m'
MAGENTA = '\033[38;5;201m'
DARK_GRAY = '\033[38;5;236m'
BOLD = "\033[1m"

print(f"""{BOLD}{VIOLET}
   _____ __                 ______          __           ___________ _________    ____  ______       ____  ____  ____  __  ___       ___ ____ 
  / ___// /_  ________  ___/_  __/__  _____/ /_         / ____/ ___// ____/   |  / __ \/ ____/      / __ \/ __ \/ __ \/  |/  /      <  // __ \ 
  \__ \/ __ \/ ___/ _ \/ _ \/ / / _ \/ ___/ __ \       / __/  \__ \/ /   / /| | / /_/ / __/        / /_/ / / / / / / / /|_/ /       / // / / /
 ___/ / / / / /  /  __/  __/ / /  __/ /__/ / / /      / /___ ___/ / /___/ ___ |/ ____/ /___       / _, _/ /_/ / /_/ / /  / /       / // /_/ / 
/____/_/ /_/_/   \___/\___/_/  \___/\___/_/ /_/      /_____//____/\____/_/  |_/_/   /_____/      /_/ |_|\____/\____/_/  /_/       /_(_)____/  

2026 version 1.0 2026-VER-1.0                                                                                                                                          
{RESET}""")

print(f"{RED}OSIRIS HAS GONE ROGUE!!\nThey all screamed at the top of their lungs as their once high tech laboratory is now in ruble as OSIRIS-Vr_99X steps from the ruble\nOSIRIS SCREANS IN A ROBOTIC VOICE\n'LETS TEST YOU EARTLINGS BRAIN!'\nThat was all i heard as huge white walls surrounded us with a lever next to a keypad their was also a sign i notice below the keypad that said-\n'HAHAHA! YOU ARE NOW TRAPPED IN MY ESCAPE ROOM GUESS MY CODE IN 3 TRIES OR YOU ALL DIE!")

code = 2026

guess1 = input(f"{AQUA}Choose your first guess: ")

if guess1 == '2026':
    print(f"{GREEN}HOW?! FIRST TRY!\nThe robot screamed but was cut of by a\nBANG!\nthe shotgun in professor Sadrick explained it all\nTHE ROBOT IS DEAD HUMANITY WINS!")
else:
    guess2 = input(f"{AQUA}A LOUD BOOMING WALLS CAME THAT SHOOK THE ROOM!\nHAHA I KNEW YOU EARTHLINGS WERE USELESS AT LEAST YOU DONT KNOW THE CODE STARTS WITH 20 HAHA-- OH SHOOT...\nMAKE YOUR NEXT GUESS: ")

if guess2 == '2026':
    print(f"{GREEN}HOW?!\nThe robot screamed but was cut of by a\nBANG!\nthe shotgun in professor Sadrick explained it all\nTHE ROBOT IS DEAD HUMANITY WINS!")
else:
    guess3 = input(f"{RED}A LOUD BOOMING WALLS CAME THAT SHOOK THE ROOM!\nHAHA I KNEW YOU EARTHLINGS WERE USELESS AT LEAST YOU DONT KNOW THE CODE IS THIS YEAR-- OH SHOOT...\nMAKE YOUR NEXT GUESS: ")

if guess3 == '2026':
    print(f"{GREEN}BREALY MADE IT YOU IDIOTS!\nThe robot screamed but was cut of by a\nBANG!\nthe shotgun in professor Sadrick explained it all\nTHE ROBOT IS DEAD HUMANITY WINS!")
else:
    print(f"{RED}{BOLD}I felt something drop in my stomach as our 3rd try beeped a read light\nBefore i could realize anything i knew i was dead!")
    print(r"""
 _____   ___  ___  ___ _____   _____  _   _ ___________ _ 
|  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \ |
| |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ / |
| | __ |  _  || |\/| ||  __|  | | | || | | |  __||    /| |
| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \|_|
 \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_(_)
                                                                                                                  
""")
