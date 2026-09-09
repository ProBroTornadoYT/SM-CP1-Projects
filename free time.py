import random

ask = print("Type'Heads' or 'Tails' ")


flip = random.randint(1,2)

if flip == 1:
    print("Heads!")
else:
    print("Tails!")

if ask == flip:
    print("You WON!")
else:
    print("You lost")