import random

ask = print("Your  ")


flip = random.randint(1,2)

if flip == 1:
    print("Heads!")
else:
    print("Tails!")

if ask == flip:
    print("You WON!")
else:
    print("You lost")