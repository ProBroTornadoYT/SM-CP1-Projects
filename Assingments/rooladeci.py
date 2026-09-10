#SM Die roller
import random

print("WELCOME TO THE DICE ROLLER PLEASE TYPE YOUR DIE TYPE BELOW!!")
user_input = input('What size dice would you like to roll? (D4, D6, D8, D10, D12, D20,D100000:')

if user_input == 'D4':
    d4= random.randint(1,4)
    print(d4)


if user_input == 'D6':
    d6= random.randint(1,6)
    print(d6)


if user_input == 'D8':
    d8= random.randint(1,8)
    print(d8)


if user_input == 'D12':
    d12= random.randint(1,12)
    print(d12)


if user_input == 'D20':
    d20= random.randint(1,20)
    print(d20)



if user_input == 'D100000':
    d100000= random.randint(1,100000)
    print(d100000)

