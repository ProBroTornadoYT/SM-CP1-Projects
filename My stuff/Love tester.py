#love tester

import random

person1 = input("Type your first person: ").strip().title()
person2 = input("Type your second person person: ").strip().title()

love = random.randint(70,120) 

print(f"Looks like {person1} loves {person2} at about {love}% love oooh")

if love > 100:
    print(f"Oh dayum {love}% love is more than 100! thats a match made in heaven")

if love == 120:
    print("120 percent!!!!!! thats THE MAX AMOUNT OF LOVE!!!!")