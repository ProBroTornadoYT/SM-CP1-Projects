import sys, time, random
#SEVEN CARD CHARLIE!!!
import os

def clear_terminal(): #this clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

slug=[ #big slug art
"                                               :===-:                                      -+*#*=-             ",
"                                              +#%%####=-                                  *#%%#%#*=            ",
"                                              =###***%##+-   :=++==-:-=+#*=-:=--         +##*++*##*=           ",
"                                              =###***#%###+--*%%#%%#**#%%%%##%%%*=     -+##++++#%#*=-          ",
"                                              :*%#*****+#%#*####*++#%##++*#%#*+*%#=: ::+#*++*+++*##+-          ",
"                                              -#%#*****+*##%%%***++*%%*+**##*++*#%%%%##%%#++*++**##+-          ",
"                                        -+*#######*****#***####*++*#%%%**#####%**###*####**##*+++*#+           ",
"                                       -*######%%%#**++#%**##%#***##**#%%%#**%##**#*++##++*##*++*##+           ",
"                            ---        =###****##%%#****#%***##**##**#**##*++++++*#****%**##*++**#*=           ",
"                          +*%%###*+--- -*####%%#**#%%#***##**#%#*##*#####%#*++++**#**+*#*##**+++##+            ",
"                         +#%#***#####***%%#*##%%#**#%%#**##**###*##****+*%*+++++*##***#####+++*#%*             ",
"                         +####%%##**#%%%%%%##*******#%%%####*####%##****##*+++++*##*+*%###****##=              ",
"                          +#####%##*#**#%%%%####*****#%%%%%%##**+++**###%##******##**#%####%%%%%*+-            ",
"                  ===++=+=+#%#***##############%##***#%*+===+*########***+*####%%%%%%%%%%#*+==-=*#*=           ",
"                 =*#%#%#%%%%%%%%%%#########*#####%%##+-=+#%#*****#******##%#*+=--------=+#########%*+-         ",
"                 +##***#####%%%%%%%%%%%%#%########*=-+#%#******######%###***####*=----+%#***#####**##*+        ",
"                -=*%##%%%%%#*##%%#####%%%%%%##*%%+-=*##***###%%#*+===++*##%##***##*++##**##*+++####**#*=       ",
"             -+**##%%%#####*########%%%##*##%%%+--=*%#***###*=::::::::::::-+#####**##**#%#=:::::-=###**#+-     ",
"            =*%%####%%%%%%######%%###########%+---+#*****##=:::::::::::::::::-+##%####%#+-::::::::-*%#**#*=    ",
"            -#%###%%%%#####%%%#%%%%%%%%####%#=---+#*++**##=:::::-=****=-::::::::-=+++=-::::---::::::+##**#*+   ",
"             =*%################*#######%%%#=---=*#*++*##=::::-+#####%##*-::::::::::::::-*###%#*+-::-=%##*#+=  ",
"               +*#%%##*######%%###%%###*###+----=##+++#%*-:::=*#####+--=+*=::::::::::::=#%%%*-:=#+::::=##**#=  ",
"                  ++*#%%%%%%%%%%%##*#######=----+#*+++#%+:::-*###%%*=:.:+#+-::::::::::=#####+:.-**=::::*##*#*- ",
"           :=+####%#***#%####%###%%%%###%%*-----+#*+++##+:::-####%%##**###*-::::::::::+#####%#####+-:::=##**#= ",
"           +#%####%%#%%%####%%##***###%%%#=-----+%*+++##*:::-*#####%######*-::::::::::+######%####+::::-##**#*-",
"           *##**#%%%#*###%%#############%*=-----+%*+++##+-::-+######%%####+-::::::::::-####%#####*-::::-*#*+*#=",
"           -+##########**###%%%%%##%%%%%%*--:---=##+++*%*-:::-+#%#########=::::::::::::-+####%%*-::::::-*#*+*#=",
"               =+*%%%######*#%######%####*-------*#*++*##+::::::=*######*=::==--::::=+-::-=+==-::::::::-*#++##=",
"                 #%%%%%%%%%%###%####%##%#=-------*%#*++*#*-:::::::::::::::::=%%+-::=#%=::::::::::::::::+##+*#*:",
"                 #%%%%%%%%%%###%####%##%#=-------*%#*++*#*-:::::::::::::::::=%%+-::=#%=::::::::::::::::+##+*#*:",
"                *#%##%%%#*##%%%%%%%######-------:-##**++##=:-::::::::::::::::-+%%%%%*-::::::::::::::::+%#*+##+ ",
"           -=++**%#########%%%#####%%%%#*--------:+##****#*-:::::::::::::::::::::::::::::::::::::::::+%#+**#*= ",
"          =*%%####%%%%%%########%%%#*###+----------*%#**+*#+-::::::::::::::::::::::::::::::::::::::-+%#++*#%*  ",
"          +##############%%%%%##########=--:--------*%##**##+-::::::::::::::::::::::::::::::::::::=#%*+**#%*+  ",
"          -*####%%%###*#**###%%%%%###%%*-------------*%#***#%*-::::::::::::::::::::::::::::::::::=##++*####*   ",
"            =*#%%#################%%%##+--------------*%##**#%*=::::::::::::::::::::::::::::::::+%#***##*#*+   ",
"               -+#%%%%#%%%%###%%%#**###=---------------*%#***###+-::::::::::::::::::::::::::::=#%****%*=*%#    ",
"               =#%##%######%##%%#####%*-----------------*%##***##+-:::::::::::::::::::::::::-*%#+**##=-+##-    ",
"               *####%%######%%%%%%%%##=-----------------=###****##+-:::::::::::::::::::::::=##*+++*#+-=##+     ",
"               -+#%########%%##%#####+-------------------+##***++*#+-:::::::::::::::::::::=##++++*#+--+##      ",
"                =*#%%%%%%%%%%%%%%##%#=--:-----------------*%*++++*##+::::::::::::::::::::=##*++++**--=##=      ",
"                +####%%####**%%#*###=---------------------+#*+++++*##=::::::::::::::::::-*#*++++*#+:-*#*:      ",
"                =+##%%%######%#==*%*----------------------+#*++++++*#*-:::::::::::::::::=##*++++*#+-=*#=       ",
"               =+##*++**###%%%*=*%#=--=*###%%%%####*++++**###***+++###+-::::::::::::::::-*#*+++++#*-=##-       ",
"            :-+##*=-----=+#%%%++##==*#%%##############%%%%%##******###*-::::::::::::::::-+#****++*#+=##-       ",
"           =*##+=------+##+=**+####%%################%%%%####*****##%##-:::::::::::::::::-##******#%*##=       ",
"         :=*#*=---------=---=+#%%#%###*#######*#############**##*#%**##=::::::::::::::::::=###*****#%%#+:      ",
"        ++*#+=--------------+#%%%############################*##%#+=*#*-:::::::::::::::::::-*#%%#***##%#*=     ",
"     -+##%%#=--------------=*%%%############%%%%%%%%%%%%%%%%%%#*+=-+#%=:::::::::::::::::::::::-+*%##***###+    ",
"   =**%%%##*=------------=+*%%%#**#######%#*+=-=-------=====------=*%*:::::::::::::::::::::::::::-*%#****##+-  ",
" -+#%%***###*+=--------=*#%%%######*#%%%*=-----------------------=*#*-:::::::::::::::::::::::::::::=#%#***#%*= ",
"=+#%#******#%%%%#####%%%%%########%%#*=-----==+++====----------=+##=::::::::::::::::::::::::::::::::-##***+##*:",
"=*%#*******#*################**#%%*=---==+#%#*++++**####*+++**###=-::::::::::::::::::::::::::::::::::+##**+*##=",
"=*###**######################%%#+=----=*%#=:::::::::::::::----:::::::::::::::::::::::::::::::::::::::=##*++*##=",
" +#%######################%%#+=-----=*#%+::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::=##*++*%# ",
"   *#%%%#############%%%%#+---------=%#+::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-#%*++*%#= ",
"      -+##%%%%%%##**++==------------=##=:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-*#*+*#%#   ",
"          +#%*+=---------------=*+=--+#*-:::::::::::::::::::::::::::::::::::::::::::::::::::::::::=*##%%%#     ",
"            *#%#*+==-----------=+#%#+==##+-:::::::::::::::::::::::::::::::::::::::::::::::::::::=*%%*+=        ",
"              -*###%%##**********##%%%###%%#*++==+========------==-------------------------++*#%%%*            ",
"                    +****########%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%#+-                "
]
wizard_slug=[
"                                                             -=+=-:                                                                         ",
"                                                           -++#%%#***=:                                                                     ",
"                                                           ++#%##%%%*+=+-                                                                   ",
"                                                            ##%# :#%@#*==+-                                                                 ",
"                                                             +#%: :*%@#*+-=+                                                                ",
"                                                              +#@: -*%@%*+-=+-                                                              ",
"                                                               *#*  +#@%***==+=                                                             ",
"                                                             -=*%+  =+%%#+*+=+-+                                                            ",
"                                                              -*:   :#%%#***++#=*:                                                          ",
"                                                                    :%%%#*+++=*#**-                                                         ",
"                                                                    =%%%#*+++=+*#**=                                                        ",
"                                                                    +%##%*+++=++*#**=:                                                      ",
"                                                                   :##*+**##*=+++#%*+=:                                                     ",
"                                                                   =%##%%%#++++++*%%#++:                                                    ",
"                                                                  -#%@%##*+++++++*%%%#*+=                                                   ",
"                                                           ::    :#%@@@%#*+++++++#%%%%##-=         :==:                                     ",
"                                                         :*#%#*+-##@@@%#*+++++++*#+#%%%##+=      -*%%%#*:                                   ",
"                                                         =##***#%+%@@%##*+++****##+=#%@@%#++    +##*++*#*:                                  ",
"                                                         =##****%#@@%%###++##+=-::::-++#@%#%%*###*+++*%%%#####=                             ",
"                                                         :*##***+%%@%####*++*%%%#*+-+#%@%%%%%@**#%#########%%##                             ",
"                                                      ::-=###**#%#*#%#####*++*#%*=#*###%%%%%@%#%#%**######*##%+                             ",
"                                                 :=*#%%@@@@%%%#*@%%%%%#*#####**%*#@@@%#@%%#%##%@%######*%%%*##:                             ",
"                                               :*%@@%***#%%###%%@@%%%%%%%%####%@@%%%%%@@%*###%@%##**###%%*#%#:                              ",
"                                        =**+-::+%@%%%%%%%%#%@#@@=%%%@%%%%%%%###%%@@%%*+**%%@@@##*++*####*%%*                                ",
"                                      -*%##*#####%%%%%%%%%%%@@@@@%%%*+++#****+===+++*##%@@@%%**+=+*####%#+                                  ",
"                                      =#######*##%%%%%#%%%%%%%%@@@@%%%%%###**####%%%@@@@@%#*+++**####%%+                                    ",
"                                       +####%##*#%#%%%@%%%%%%%%@@%@@@@@@@@@@@@@@@@@@%#*#*+++*###*#%#%%#-                                    ",
"                                :==+=+=+%%##*######%###%%%%%%%%*%%%%%%%%%%@@@@@%%%####**####**#%%##=--=#*-                                  ",
"                               +#%####%%%%%%%########%##%%%%%%%%%%%%%%%%%%%%###########***#%%%%%########%#=                                 ",
"                              :##########%%%%%%##%%%%%######%%@@%@@@@%%%%#*############%%%%***#**######**##*-                               ",
"                             ::=#####%%#########%%%###%%#%#++#%**#%%%#%@@@@@%@@@%@@@%#%%*##*##*###-::=*%##***=                              ",
"                           =#%%%%%%%#############%%#####%#=-=*##**#%@@@@%#***#%%%*--=*%###*#*##%+:::::::=##***=                             ",
"                          -#%########%%%%%%%%%%%%#*####%*=--+##***##=:::::-----:::::::-=##%%%#+-:::::::::=###*#+                            ",
"                           =####%%%#####%%######%%%%%%%*---=##+++##+-:::-+######+-::::::::::::::-=***=-:::-*#**#+                           ",
"                            :+#%######*##%###%%%#####%#----+#*++*#*-::-+######++**-:::::::::::-*#%%*=+#+:::-*#**#=                          ",
"                               :=#%%%%%%%%%%%%######%%=---=##*++##+:::=*##%%#=:.-**::::::::::-*####=::+#=-::=##***:                         ",
"                          :=#*###***%%#####%%%%%###%%*----=##+++##+:::+#######**###+:::::::::=###%######+-::-*#*+*+                         ",
"                         -#%%##%%%%%#%##%%%######%%%#+----=##*++##=:::=############+:::::::::=######%###+::::=#*+**                         ",
"                         -####%%%#####%%######%####%#=----=##*++*#+-::-*#####%%###*-:::::::::-*########*-::::=##+*#-                        ",
"                          :+#############%%%####%%%#*------##*+++%+-:::-*####%%###=::::::::::::+#####*-::::::=##+*#-     :.:=-              ",
"                              =*%%%%%#####%###%%%###*------=%#+++*#=::::::=*####***+++**:+*+=+**-:--::::::::-+#++*#:   -=-:-=+=             ",
"                             :+%%###%#%%%%#%%%####%#+-------*#**+*#*-::::::::::=*-.....:+:.....:*+::::::::::=#*+*#*   -**+++*##-            ",
"                           ::-*###%%%####%%%%%%%%%##=-------=##**+*#++***#=::-++:....... .......:=*-::-#****##++*#=   :=*#*###+             ",
"                         =####%%%%#######%###%%##%##---------+##***##=:-#*++*+:.:....... .......:.:+++++#=.-*+**#*:    -#***:               ",
"                        :*%##########%%%%%#########*----------+##***#:........:.......::::........:....:...:+**##-     =+**=                ",
"                         =###%%%%#########%%%######=---:-:-----*##**#=:...   ..:.:::=*#=:-**=::..:..    ...=####*:    :+#*:                 ",
"                           +#%%*########%#####%%%#%-------------+%#**#*-:..:..:::=*+....   .:+*=::.......:+##*##-     -*#=                  ",
"                             -*%%%%%%%%%##%%%#####+--------------+##***##*++++++=...:......  .:.-++++++**###++#*     -**=                   ",
"                            :*%##%%######%%%#####%----------------*##***##-:.......:......::...:........-##-=**      =*=                    ",
"                             +##########%%##%%%%#+----------------=#%#**#=........::..:.  .::...:.:...:.:*=-+#=      **:                    ",
"                              :*%%%%%#####%%%##%#=-----------------+##***:....:...:...:.   .:....:.::.: .++-**:     **=                     ",
"                              +%##%%###%#%%%%#%#+-------------------*#**=..:..:.:.:.:.:..:...:.....:..:..-#+#=     =#=                      ",
"                              =##%%%%######*=*#*=-------------------*##*-..:..:.:...:.:...:..:..:....::. :##*:    -**                       ",
"                              =#%##%####%%#++##=---=+*###*+++==-=-==*##*--:::.:....::.:..:.:....:.  .::. .*#*    -**:                       ",
"                            =##+----===#%%#+#%+-+#%%#########%%%%%%%%###*-:::::...:.:.....:.:...::..::.: .+#+    =#=                        ",
"                          +*#+=-----+##*=#**##*#%###############%########-::::::..:.:.....::.:..::.::..::.+%*:  :*=                         ",
"                        :+#*=-------==---+*##%%##########################=::::::..:..:.. .:::...:::::.:.-+*%*-  +*:                         ",
"                      -+*#+=------------=*#%%############################+::.::::::..::. .:.::..:::::.:.=#%###=+*-                          ",
"                   :=#%%##=------------=+#%%###########%%#########%#%##*+#-..:::::::...::.:..:..:.::::.:*#***###*                           ",
"                  =*%%#*##=-----------+#%%%########%%*=------------------=#-.-:::::::....::..::::.:=-.-**#%#***##=                          ",
"                -*#%****####++====++##%%%#######%#*=---------------------=+#=:=:::::::....:...::..-*=+*-::+%###*##+                         ",
"               :*%#*******##%%%%%%%%###########*=---==+**#####*++===-==+*##+=*=++-:.:::..::...::.:*#*-:::::*###**##:                        ",
"               :*##****###################%%#+=---=*#*=-:::::::-===++++==-::::-+###+:..:::=:....-#+=:::::::+##**+*#=                        ",
"                =%#####################%%#+=----=*##=::::::::::::::::::::::::::::::-**-:.:+=..-*+:::::::::+*##*++##:                        ",
"                  +#%##############%%%*=--------+##-::::::::::::::::::::::::::::::::::+*--*==*+::::::::::=####**##=                         ",
"                    :-+*%%%%%###**+=------------+##-:::::::::::::::::::::::::::::::::::-#*#+-::::::::::::-#%#*##*-                          ",
"                        :+##+==------------=**===+%+::::::::::::::::::::::::::::::::::::-+::::::::::::::=#%%%#=:                            ",
"                          :+##*++====------==*%##++%#+-::::::::::::::::::::::::::::::::::::::::::::::-+##+-:                                ",
"                             :-+#%%%%%%%%%%%%%%%%%%%%%%%%##############*####*#######********#+*++*#%%%#-                                    ",
"                                              :::::::-=------===============+=+=++++++++=+++*++=-:                                          "
]

ascii_word=[
    " ________  _____  _______     ________  ______        _       _____     _____     ",
    "|_   __  ||_   _||_   __ \\   |_   __  ||_   _ \\      / \\     |_   _|   |_   _|    ",
    "  | |_ \\_|  | |    | |__) |    | |_ \\_|  | |_) |    / _ \\      | |       | |      ",
    "  |  _|     | |    |  __ /     |  _| _   |  __'.   / ___ \\     | |   _   | |   _  ",
    " _| |_     _| |_  _| |  \\ \\_  _| |__/ | _| |__)  _/ /   \\ \\_  _| |__/ | _| |__/ | ",
    "|_____|   |_____||____| |___||________||_______/|____| |____||________||________| "
]

deck=[ #the ENTIRE deck, no jokers
    [" _____ ",
    "|\\   /|",
    "| \\ / |",
    "|  &  |",
    "| / \\ |",
    "|/___\\|"],

    [" _____ ",
    "|A .  |",
    "| /.\\ |",
    "|(_._)|",
    "|  |  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  ^  |",
    "|     |",
    "|  ^  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| ^ ^ |",
    "|     |",
    "|  ^  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| ^ ^ |",
    "|     |",
    "| ^ ^ |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| ^ ^ |",
    "|  ^  |",
    "| ^ ^ |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| ^ ^ |",
    "| ^ ^ |",
    "| ^ ^ |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| ^ ^ |",
    "|^ ^ ^|",
    "| ^ ^ |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|^ ^ ^|",
    "| ^ ^ |",
    "|^ ^ ^|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|____6|"],

    [" _____ ",
    "|10 ^ |",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|^ ^ ^|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| ^ {)|",
    "|(.)% |",
    "| | % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| ^ {(|",
    "|(.)%%|",
    "| |%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| ^ {)|",
    "|(.)%%|",
    "| |%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A _  |",
    "| ( ) |",
    "|(_'_)|",
    "|  |  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  &  |",
    "|     |",
    "|  &  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| & & |",
    "|     |",
    "|  &  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| & & |",
    "|     |",
    "| & & |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| & & |",
    "|  &  |",
    "| & & |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| & & |",
    "| & & |",
    "| & & |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| & & |",
    "|& & &|",
    "| & & |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|& & &|",
    "| & & |",
    "|& & &|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|& & &|",
    "|& & &|",
    "|& & &|",
    "|____6|"],

    [" _____ ",
    "|10 & |",
    "|& & &|",
    "|& & &|",
    "|& & &|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| o {)|",
    "|o o% |",
    "| | % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| o {(|",
    "|o o%%|",
    "| |%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| o {)|",
    "|o o%%|",
    "| |%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A_ _ |",
    "|( v )|",
    "| \\ / |",
    "|  .  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  v  |",
    "|     |",
    "|  v  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| v v |",
    "|     |",
    "|  v  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| v v |",
    "|     |",
    "| v v |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| v v |",
    "|  v  |",
    "| v v |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| v v |",
    "| v v |",
    "| v v |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| v v |",
    "|v v v|",
    "| v v |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|v v v|",
    "| v v |",
    "|v v v|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|v v v|",
    "|v v v|",
    "|v v v|",
    "|____6|"],

    [" _____ ",
    "|10 v |",
    "|v v v|",
    "|v v v|",
    "|v v v|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "|   {)|",
    "|(v)% |",
    "| v % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "|   {(|",
    "|(v)%%|",
    "| v%%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "|   {)|",
    "|(v)%%|",
    "| v%%%|",
    "|_%%%>|"],

    [" _____ ",
    "|A ^  |",
    "| / \\ |",
    "| \\ / |",
    "|  v  |",
    "|____V|"],

    [" _____ ",
    "|2    |",
    "|  o  |",
    "|     |",
    "|  o  |",
    "|____Z|"],

    [" _____ ",
    "|3    |",
    "| o o |",
    "|     |",
    "|  o  |",
    "|____E|"],

    [" _____ ",
    "|4    |",
    "| o o |",
    "|     |",
    "| o o |",
    "|____h|"],

    [" _____ ",
    "|5    |",
    "| o o |",
    "|  o  |",
    "| o o |",
    "|____S|"],

    [" _____ ",
    "|6    |",
    "| o o |",
    "| o o |",
    "| o o |",
    "|____9|"],

    [" _____ ",
    "|7    |",
    "| o o |",
    "|o o o|",
    "| o o |",
    "|____L|"],

    [" _____ ",
    "|8    |",
    "|o o o|",
    "| o o |",
    "|o o o|",
    "|____8|"],

    [" _____ ",
    "|9    |",
    "|o o o|",
    "|o o o|",
    "|o o o|",
    "|____6|"],

    [" _____ ",
    "|10 o |",
    "|o o o|",
    "|o o o|",
    "|o o o|",
    "|___0I|"],

    [" _____ ",
    "|J  ww|",
    "| /\\{)|",
    "| \\/% |",
    "|   % |",
    "|__%%[|"],

    [" _____ ",
    "|Q  ww|",
    "| /\\{(|",
    "| \\/%%|",
    "|  %%%|",
    "|_%%%O|"],

    [" _____ ",
    "|K  WW|",
    "| /\\{)|",
    "| \\/%%|",
    "|  %%%|",
    "|_%%%>|"],
]

house_hand=[] #setting the house hand to nothing
player_hand=[ #we will need the blank card for later
    ["       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "       "]
]
#setting important variables and lists
player_value_history=[]
house_value_history=[]
current_player_value=0
current_house_value=0
bet_amount_history=[]
money_list=[1000]

def typer(text):
    for char in text: #for character in text
        speed=random.randint(250,750)/random.randint(5000,15000) #the speed at which the typer types, take a number between 250 and 750 and divide it by a number between 5000 and 15000
        print(char,end="") #print the one character and don't go to a new line
        time.sleep(speed) #wait for an extra random amount of time to add a human feel
    print("") #go to a new line

def house_valuefinder(card):
    decklen=len(deck) #get the length of the deck because it will change over time
    chosenh_card=random.randint(1,decklen-1) #get a random number between the 2nd card (the first is the overturned one) and the last card
    house_hand.append(deck[chosenh_card]) #put the chosen card in the player hand
    del deck[chosenh_card] #delete it from the deck

    #this chunk checks the second line of the card for a specific character
    if "A" in house_hand[card][1]:
        hc_value=1
    elif "J" in house_hand[card][1] or "Q" in house_hand[card][1] or "K" in house_hand[card][1]:
        hc_value=10
    elif "2" in house_hand[card][1]:
        hc_value=2
    elif "3" in house_hand[card][1]:
        hc_value=3
    elif "4" in house_hand[card][1]:
        hc_value=4
    elif "5" in house_hand[card][1]:
        hc_value=5
    elif "6" in house_hand[card][1]:
        hc_value=6
    elif "7" in house_hand[card][1]:
        hc_value=7
    elif "8" in house_hand[card][1]:
        hc_value=8
    elif "9" in house_hand[card][1]:
        hc_value=9
    elif "10" in house_hand[card][1]:
        hc_value=10
    return hc_value

def player_valuefinder(card): #this is the same as house_valuefinder but for the player
    decklen=len(deck)
    chosenp_card=random.randint(1,decklen-1)
    player_hand.append(deck[chosenp_card])
    del deck[chosenp_card]
    if "A" in player_hand[card][1]:
        hp_value=1
    elif "J" in player_hand[card][1] or "Q" in player_hand[card][1] or "K" in player_hand[card][1]:
        hp_value=10
    elif "2" in player_hand[card][1]:
        hp_value=2
    elif "3" in player_hand[card][1]:
        hp_value=3
    elif "4" in player_hand[card][1]:
        hp_value=4
    elif "5" in player_hand[card][1]:
        hp_value=5
    elif "6" in player_hand[card][1]:
        hp_value=6
    elif "7" in player_hand[card][1]:
        hp_value=7
    elif "8" in player_hand[card][1]:
        hp_value=8
    elif "9" in player_hand[card][1]:
        hp_value=9
    elif "10" in player_hand[card][1]:
        hp_value=10
    return hp_value

#this whole thing prints the cards
def custom_printer(hidden):
    print("")
    printer_helper=0 #a little helper variable for later
    def seven_card_charlieplayer():
        #each segment will try to print the first line of the first, second, third, etc card, if it doesn't work we print nothing. example:
        # _____   _____
        #|K  WW| |K  WW| then nothing over here, unless we have another card
        #| o {)| | /\{)|
        #|o o%%| | \/%%|
        #| |%%%| |  %%%|
        #|_%%%>| |_%%%>|

        try:        
            print(player_hand[1][printer_helper], end=" ") #printer helper is telling us which row of the card to print
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[2][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[3][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[4][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[5][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[6][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(player_hand[7][printer_helper])
        except IndexError:
            print(player_hand[0][0])

    def seven_card_charliehouse(hidden):
        #this is for the house
        if hidden=="yes": #if we are hiding the first card, then we do this section
            try:        
                print(deck[0][printer_helper], end=" ") #see "deck" and not "house_hand?" that first card of the deck is the turned over card
            except IndexError:
                print(player_hand[0][0], end=" ")
        if hidden=="no": #if not, we do this
            try:        
                print(house_hand[0][printer_helper], end=" ") #now it's house_hand and not deck
            except IndexError:
                print(player_hand[0][0], end=" ")
        #the rest of it is the same as the player's
        try:
            print(house_hand[1][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[2][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[3][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[4][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[5][printer_helper], end=" ")
        except IndexError:
            print(player_hand[0][0], end=" ")
        try:
            print(house_hand[6][printer_helper])
        except IndexError:
            print(player_hand[0][0])
    typer("House cards:")
    time.sleep(0.5)
    for item in player_hand[0]:
        if hidden=="yes": #if the argument equals yes we hide the first house card
            try:
                seven_card_charliehouse("yes") #do the thing
                printer_helper+=1 #add one to printer helper
            except IndexError:
                print(item) #if something weird happens this is a failsafe, which should NEVER activate but here it is
        if hidden=="no": #same thing as before but we don't hide the first house card
            try:
                seven_card_charliehouse("no")
                printer_helper+=1
            except IndexError:
                print(item)
    printer_helper=0 #set printer helper back to 0
    typer("Your cards:")
    time.sleep(0.5)
    for item in player_hand[0]: #print our cards
        try:
            seven_card_charlieplayer()
            printer_helper+=1
        except IndexError:
            print(item)

pcard_1=player_valuefinder(1) #getting the player's first card, it's 1 and not 0 because of the blank card already in player_hand
hcard_1=house_valuefinder(0) #getting the house's first card

pcard_2=player_valuefinder(2)
hcard_2=house_valuefinder(1)

def money_updater(winorlose,money,bet_amount): #this will update our money
    helper_variable="no"
    if winorlose=="p": #if we win we add the bet_amount to our money
        money=money+bet_amount
    elif winorlose=="h": #if we lose we subtract it
        money=money-bet_amount
        if money<=0: #if we go under $0 then we lose and end the program, this means the game won't end unless the player loses all their money
            time.sleep(1)
            typer("You ran out of money.")
            time.sleep(0.75)
            government_chance=random.randint(1,3)
            paycheck=random.randrange(250,750,50)
            typer(f"A paycheck just came in for you, giving you ${paycheck}.")
            time.sleep(1)
            if government_chance==1:
                typer("Unfortunately, the government took your entire paycheck because you didn't pay taxes.")
                time.sleep(0.75)
                typer("You are truly out of money.")
                sys.exit()
            else:
                typer(f"${paycheck} has been added to your balance.")
                money_list.clear()
                money_list.append(paycheck)
                helper_variable="yes"
    elif winorlose=="t": #if we tie then money now equals money
        money=money
    time.sleep(2.5)
    if helper_variable=="no":
        money_list.clear() #clear the money list
        money_list.append(money) #add the new money value to it so the only value in it is now the new money

def betting_time(): #this will handle when the player is betting money
    time.sleep(1)
    typer("How much money do you want to bet?")
    ok_to_break="n"
    while True: #a while True loop so if they don't give us the answer we want we trap them :D
        try:
            bet_amount=int(input("$")) #try inputting an integer
            time.sleep(0.75)
        except:
            typer("Please input a number.") #if it isn't an integer then we ask to input a number
        else:
            if bet_amount>money_list[len(money_list)-1]: #if the bet amount is more than what the player currently has
                typer("You cannot bet more than what you have.") #we tell them they can't bet more than what they have
            elif bet_amount<=0: #we don't want them to bet $0 and never lese
                typer("Please input a number above 0.")
            elif bet_amount==money_list[len(money_list)-1]:
                while True:
                    typer("Are you sure you want to go all in?")
                    all_in_question=input("")
                    if "ye" in all_in_question:
                        ok_to_break="y"
                        break
                    elif "no" in all_in_question:
                        time.sleep(0.75)
                        typer("How much money do you want to bet?")
                        break
            else:
                ok_to_break="y"
            if ok_to_break=="y":
                break #if everything is good then we break the loop
    bet_amount_history.append(bet_amount) #add the nice and neat bet_amount to the bet_amount_history

def win(who): #if someone wins we call this function
    won=[ #just some art
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|             You win!              |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
    ]
    lost=[
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|             You lost!             |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
    ]
    tie=[
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|            It's a tie.            |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|                                   |",
    "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"
    ]
    if who=="p": #if the player won
        for item in won:
            print(item) #print the player win art
    elif who=="h": #if the house won
        for item in lost:
            print(item) #print the player lost art
    elif who=="t": #if it's a tie
        for item in tie:
            print(item) #print the tie art
    money_updater(who,money_list[len(money_list)-1],bet_amount_history[len(bet_amount_history)-1]) #call the money_updater function

def win_checker_forstart(first_num, second_num): #this function will be called at the start twice to see if the player or house has blackjack
    win=0 #setting win
    if first_num==1 and second_num==10: #if the first card's value is 1 and the second card's value is 10
        win=1 #win is now 1
    elif first_num==10 and second_num==1: #if the first card's value is 10 and the second card's value is 1
        win=1 #win is now 1
    return win #return the value of win to whatever called the function

def player_value_calculator(firstnum, secondnum): #this function will be very useful
    current_player_value=firstnum+secondnum #current_player_value=the first number plus the second number
    player_value_history.append(current_player_value) #add current_player_value to player_value_history
    return current_player_value #return current_player_value

def house_value_calculator(firstnum, secondnum): #the same as the other one but for the house
    current_house_value=firstnum+secondnum
    house_value_history.append(current_house_value)
    return current_house_value

will_it_fireball=random.randint(1,25)
#finally, we are at the game
if will_it_fireball==1: #just some funny stuff
    for item in wizard_slug:
        print(item)
    time.sleep(0.5)
    for item in ascii_word:
        print(item)
else:
    for item in slug:
        print(item) #printing the slug
time.sleep(3) #waiting, as if the slug was the loading screen
clear_terminal() #clear the terminal
typer("Welcome to Doomslug Blackjack.")
while True:
    time.sleep(0.75)
    typer("Do you know the rules of Blackjack?")
    do_they_know=str(input(""))
    if "ye" in do_they_know: #if the string "ye" is in the input
        time.sleep(0)
        break #we are happy, don't tell them the rules
    elif "no" in do_they_know: #if the string "no" is in the input
        typer("Here are the rules of this game:") #tell them the rules
        time.sleep(0.5)
        typer("1. The goal is to get as close to 21 without going over. If you start with an Ace and another card worth 10, you win instantly.")
        time.sleep(0.75)
        typer("2. Face cards are worth 10, and Aces are worth 1. Number cards are worth themselves.")
        time.sleep(0.75)
        typer("3. If you reach 7 cards without going over 21, you automatically win. This rule is called Seven Card Charlie, and it also affects the house.")
        time.sleep(0.75)
        typer("4. During your turn, you can hit or stand. Hitting means you want another card, and standing means you stop.")
        time.sleep(0.75)
        typer("5. The house will continuously hit until they reach 17 or any number higher than 17.")
        break #we are happy
    #if we don't find what we are looking for then we loop

#this is the actual game code, it has many nested functions
def actual_game():
    time.sleep(1)
    typer(f"You have ${money_list[len(money_list)-1]}.") #tell them how much money they have
    betting_time() #it's betting time
    time.sleep(1.5)
    typer("Let's begin.")
    time.sleep(1)
    clear_terminal()
    time.sleep(0.5)
    custom_printer("yes") #print the cards, and the house's first card is hidden

    player_value_calculator(pcard_1,pcard_2) #use the calculator functions from before
    house_value_calculator(hcard_1,hcard_2)

    if win_checker_forstart(pcard_1, pcard_2)==1: #use the win checker for start function to see if they got blackjack
        typer("You got Blackjack!")
        time.sleep(1)
        win("p") #call the win function and tell it that the player won
        return #exit the actual_game function
    elif win_checker_forstart(hcard_1, hcard_2)==1: #the same function but used for the house
        typer("The house got Blackjack.")
        time.sleep(0.5)
        custom_printer("no")
        time.sleep(1)
        win("h") #call the win function and tell it that the house won
        return

    typer("Your current total card value is: ")
    time.sleep(0.25)
    typer(str(player_value_history[len(player_value_history)-1])) #tell them the sum of their cards' values

    def player_turn(player_value_helper): #the parameter here helps the player draw new cards and put them in the right spot in player_hand
        if player_value_history[len(player_value_history)-1]>=22: #if the most recent player value is greater than or equal to 22
            time.sleep(1)
            typer("You bust.")
            time.sleep(0.75)
            win("h") #call the win function, tell them the player lost
            time.sleep(1)
            return "Bust" #return "Bust" and exit the function
        def hit_stand_sequence(): #this is, you guessed it, the hit stand sequence
            while True:
                time.sleep(0.75)
                typer("Do you want to hit or stand?")
                try:
                    hit_or_stand=input(str("")) #an input with extra precautions
                except ValueError: #this is just a little stupid-proofing i like to do on every input i write
                    time.sleep(0)

                if "hit" in hit_or_stand and "stand" in hit_or_stand: #if hit and stand are both in the answer then we do nothing
                    time.sleep(0)
                else:
                    if "hit" in hit_or_stand: #if the word "hit" is in the answer
                        hit_or_stand="hit" #set the input variable to just equal "hit"
                        time.sleep(0.75)
                        break #break the loop
                    elif "stand" in hit_or_stand: #the same thing but for standing
                        hit_or_stand="stand"
                        time.sleep(0.75)
                        break
            return hit_or_stand #return the value of hit_or_stand, remember this is a function
        answer=hit_stand_sequence() #go through the hit stand sequence and get what was returned
        if answer=="hit": #we execute this code if the player wants to hit
            next_pcard=player_valuefinder(player_value_helper) #get another card for the player, using the argument given to the player turn function when it was called
            custom_printer("yes") #print the new cards, house cards are still hiddon
            player_value_calculator(player_value_history[len(player_value_history)-1],next_pcard) #get the new total value of the player's cards
            current_player_value=player_value_history[len(player_value_history)-1] #now we grab that new value and put it in a variable
            typer("Your current total card value is: ")
            time.sleep(0.25)
            typer(str(current_player_value)) #print that value
            return "Hit" #return the fact that the player hit
        elif answer=="stand": #if they stand we do almost nothing
            typer("Standing.")
            return "Stand" #return the fact that the player stood

    loop_helper=3 #this is set to 3 because if you look back on the previous code, pcard_two uses a value of 2 when calling the function it used
    while True: #loop the player taking turns until they bust using the checker built into the player turn, or stand
        player_answer=player_turn(loop_helper) #call the player turn, using loop_helper as the argument
        if player_answer=="Stand": #if they stand we break the loop
            time.sleep(1)
            clear_terminal()
            time.sleep(0.5)
            break
        elif player_answer=="Bust": #if they bust we exit the actual_game function, all of this is still in a function
            return
        elif loop_helper==7 and player_value_history[6]<22: #if loophelper gets to 7 (7 cards drawn by the player) and they still haven't busted, the player wins automatically
            typer("Congratulations. You have reach 7 cards without going over 21.")
            time.sleep(0.75)
            win("p") #call the win function and tell it that the player won
            time.sleep(1)
        elif loop_helper==7: #just some foolproofing, in case something somehow went wrong
            break
        else:
            loop_helper+=1 #if none of the if statements activate before this then we increase the loop_helper by 1 and loop

    time.sleep(1)
    typer("It is now the house's turn.")

    def house_turn(house_value_helper): #this house turn function is a watered-down copy of the player turn
        time.sleep(0.75)
        custom_printer("no") #we reveal the house's hidden card
        time.sleep(0.5)
        typer("The house's current total card value is: ")
        time.sleep(0.25)
        typer(str(house_value_history[len(house_value_history)-1])) #tell the player the house's current total card value
        time.sleep(0.75)
        if house_value_history[len(house_value_history)-1]>=22: #if that value is greater than or equal to 22 the house busts
            typer("The house busts.")
            win("p") #calling the win function and telling it the player won
            return "Bust"
        elif house_value_history[len(house_value_history)-1]>=17: #if that value is greater than or equal to 17 the house stands
            typer("The house stands.")
            return "Stand" #returning
        else: #if the previous if statements don't activate then we run this
            typer("The house will hit.")
            next_hcard=house_valuefinder(house_value_helper) #we get another card for the house
            house_value_calculator(house_value_history[len(house_value_history)-1], next_hcard) #calculate the house's new total card value


    time.sleep(1)
    loop_helper=2 #back when we got the second card for the house, the value in the parenthesis was 1. that explains why loop_helper equals 2
    while True:
        house_answer=house_turn(loop_helper)
        if house_answer=="Stand": #if the house stands
            break #break the loop
        elif house_answer=="Bust":
            return
        elif loop_helper==7 and house_value_history[6]<22: #if the house has drawn 7 cards and hasn't gone over 21
            typer("The house reached 7 cards without going over 21.")
            win("h") #we call the win function and tell it that the house won
        elif loop_helper==7: #some more foolproofing, i really don't want my code to break
            break
        else:
            loop_helper+=1 #if the if statements don't activate then we increase loop_helper by one and loop

    #getting the most recent values for the player and the house
    latest_player_value=player_value_history[len(player_value_history)-1]
    latest_house_value=house_value_history[len(house_value_history)-1]

    time.sleep(1)
    if latest_player_value==latest_house_value: #if they are the same
        typer("You got the same score as the house.")
        time.sleep(0.75)
        win("t") #it's a tie
        time.sleep(1)
    elif latest_house_value>latest_player_value: #if the house value is greater than the player value
        typer("The house got closer to 21 than you.")
        time.sleep(0.75)
        win("h") #the house wins
        time.sleep(1)
    elif latest_house_value<latest_player_value: #if the player value is greater than the house value
        typer("You got closer to 21 than the house.")
        time.sleep(0.75)
        win("p") #the player wins
        time.sleep(1)

def reset_deck(): #this function resets the player and house hands and the deck
    while len(player_hand)>1: #while the length of player hand is greater than one, remember we still want to keep the blank card
        try:
            deck.append(player_hand[len(player_hand)-1]) #try to add the most recent player hand card to the deck
            del player_hand[len(player_hand)-1] #then remove the most recent player hand card from player hand
        except: #if we get any error while doing this
            break #end this loop
    while len(house_hand)>0: #this is the exact same except the loop is while the length of house hand is greater than 0, not 1
        try:
            deck.append(house_hand[len(house_hand)-1])
            del house_hand[len(house_hand)-1]
        except:
            break

#we loop this forever so the only way for the game to actually end is for the player to run out of money
while True:
    actual_game() #call the actual game

    #after the game is through we reset these important variables. we can't do this inside a function because variables in a function can only be used in that function
    player_value_history=[]
    house_value_history=[]
    current_player_value=0
    current_house_value=0
    bet_amount_history=[]
    reset_deck() #call the reset function
    #get new cards for the player and house
    pcard_1=player_valuefinder(1)
    hcard_1=house_valuefinder(0)

    pcard_2=player_valuefinder(2)
    hcard_2=house_valuefinder(1)
    clear_terminal()