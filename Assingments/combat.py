import random



def main():
    print("Welcome to training! First I need to know some things about you!")
    name = input("What is your name?: ")
    
    while True:
        warrior = input(f"\nWhat class of fighter will you be {name}?\n1 if you are a Fighter\n2 if you are a Mage\n3 if you are a Rogue\nChoose your number: ")
        
        if warrior == "1":
            print("Great, here are your stats!\nHealth: 30\nDefense: 14\nAttack: D20 + 3\nDamage: D8 + 4")
            break
        elif warrior == "2":
            print("Great, here are your stats!\nHealth: 20\nDefense: 11\nAttack: D20 + 5\nDamage: D10 + 4")
            break
        elif warrior == "3":
            print("Great, here are your stats!\nHealth: 25\nDefense: 13\nAttack: D20 + 4\nDamage: D6 + 5")
            break
        else:
            print("INVALID INPUT")


def user_input():
    choice = input("What would you like to do?\n1. Normal Attack\n2. Wild Attack (you can double the damage but you will also take damage)\n3. Drink a healing potion (regain 9 health)\n4. Flee (You may or may not get away)")


def battle_warrior_1():
    if warrior == '1':
        opdamage = random.randint(1,20)
        totalopdamage = 0
        totalopdamage = opdamage + 3
    
    
    health = 30
    
    wild_attack_player_damage = random.randint()
    
    wild_attack_damage = totalopdamage * 2
    
    print("\nYou are being attacked by a Dire Wolf!\nYou move first!")
    
    attack = input(f"You are being attacked by a dire wolf!\nYou move first!\n\nWhat do you do?\n1. Normal Attack does {totalopdamage} damage\n2. Wild Attack (you can double the damage but you will also take damage) details: you take {wild_attack_player_damage} the wolf takes {wild_attack_damage}\n3. Drink a healing potion (get 9 health)\n4. Flee (50% chance of surviving): ")
    if attack == 1:
        wolf_damage = random.randint(500,10000)
        print(f"You attacked the dire wolf you did {totalopdamage} but the wolf did {wolf_damage}")
        if wolf_damage >= 30:
            print("You die! wolf win")
    if attack == 2:
        