#SM Die roller
import random

print("WELCOME TO THE DICE ROLLER PLEASE TYPE YOUR DIE TYPE BELOW!!")
user_input = input('What size dice would you like to roll? (D4, D6, D8, D10, D12, D20,D100000:')

if user_input == 'D4':
    d4= random.int(1,4)
else:
    print("Wait!")

if user_input == 'D6':
    d4= random.int(1,6)
else:
    print("Wait!")

if user_input == 'D8':
    d4= random.int(1,8)
else:
    print("Wait!")

if user_input == 'D12':
    d4= random.int(1,12)
else:
    print("Wait!")

if user_input == 'D20':
    d4= random.int(1,20)
else:
    print("Wait!")

if user_input == 'D100000':
    d4= random.int(1,100000)
else:
    print("Wait!")

# secret easter egg :)

if user_input == 'D67':
    d4= random.int(1,67)
else:
    print("Wait! Input a valid die number")
