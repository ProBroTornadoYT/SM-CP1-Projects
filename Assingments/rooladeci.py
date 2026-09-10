#SM Die roller
import random


print("WELCOME TO THE DICE ROLLER PLEASE TYPE YOUR DIE TYPE BELOW!!")
user_input = input('What size dice would you like to roll? (D4, D6, D8, D10, D12, D20,D100000:')

if user_input == 'D4':                         #for input d4, it will roll a random number between 1 and 4 and then print it to the screen.
    d4= random.randint(1,4)
    print(d4)


if user_input == 'D6':                         #for input d6, it will roll a random number between 1 and 6 and then print it to the screen.
    d6= random.randint(1,6)
    print(d6)


if user_input == 'D8':                         #for input d8, it will roll a random number between 1 and 8 and then print it to the screen.
    d8= random.randint(1,8)
    print(d8)


if user_input == 'D12':                         #for input d12, it will roll a random number between 1 and 12 and then print it to the screen.
    d12= random.randint(1,12)
    print(d12)


if user_input == 'D20':                         #for input d20, it will roll a random number between 1 and 20 and then print it to the screen.
    d20= random.randint(1,20)
    print(d20)


if user_input == 'D100000':                         #for input d100000, it will roll a random number between 1 and 100000 and then print it to the screen.
    d100000= random.randint(1,100000)
    print(d100000)

