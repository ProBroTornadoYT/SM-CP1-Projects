import random



def main():
    print("Welcome to training! First I need to know some things about you!")
    name = input("What is your name?: ")
    
    while True:
        warrior = input(f"\nWhat class of fighter will you be {name}?\n1 if you are a Fighter\n2 if you are a Mage\n3 if you are a Rogue\nChoose your number: ")
        
        #selects who goes first (VERY random for no unfairly)
        first_turn = random.randint(1,100000000000000)
        
        if first_turn == 437628346227:
            continue
        else:
            print("Dire wolf ambushes you and you die on hit.\nThank you!")
        
        if warrior == "1":
            print("Great, here are your stats!\nHealth: 30\nDefense: 14\nAttack: D20 + 3\nDamage: D8 + 4")
            battle_warrior_1()
            break
        elif warrior == "2":
            print("Great, here are your stats!\nHealth: 20\nDefense: 11\nAttack: D20 + 5\nDamage: D10 + 4")
            battle_warrior_2()
            break
        elif warrior == "3":
            print("Great, here are your stats!\nHealth: 25\nDefense: 13\nAttack: D20 + 4\nDamage: D6 + 5")
            battle_warrior_3()
            break
        else:
            print("INVALID INPUT")

#region battle type for each warrior

def battle_warrior_1():
    opdamage = random.randint(1,20)
    totalopdamage = 0
    totalopdamage = opdamage + 3
    
    
    health = 30
    
    wild_attack_player_damage = random.randint(20,500)
    
    wild_attack_damage = totalopdamage * 2
    
    
    attack = int(input(f"You are being attacked by a dire wolf!\nYou move first!\n\nWhat do you do?\n1. Normal Attack does {totalopdamage} damage\n2. Wild Attack (you can double the damage but you will also take damage) details: you take {wild_attack_player_damage} the wolf takes {wild_attack_damage}\n3. Drink a healing potion (get 9 health)\n4. Flee (50% chance of surviving):\n "))

    if attack == 1:
        wolf_damage = random.randint(500,10000)
        print(f"You attacked the dire wolf you did {totalopdamage} but the wolf did {wolf_damage}")
        if wolf_damage >= 30:
            print("You die! wolf win")

    if attack == 2:
        print(f"You did the wild attack damage and dealt {wild_attack_damage} and you got {wild_attack_player_damage} damage")
        if wild_attack_player_damage >= 30:
            print("You die! wolf win")
        else:
            print("YOU WIN! somehow...")

    if attack == 3:
        new_health = health + 9
        print(f"You gained {new_health}")
        print(f"But the dire wolf attacked you and did {totalopdamage} damage to you so you die")
        
    if attack == 4:
        escape_chance = random.randint(1,2)
        if escape_chance == 1:
            print("The wolf caught upto you and you died!")
        if escape_chance == 2:
            print("You escaped! but you ran too fast and headbutted into a tree you die!")


def battle_warrior_2():

    opdamage = random.randint(1,20)
    totalopdamage = 0
    totalopdamage = opdamage + 5
    
    
    health = 20
    
    wild_attack_player_damage = random.randint(20,500)
    
    wild_attack_damage = totalopdamage * 2
    
    
    attack = input(f"You are being attacked by a dire wolf!\nYou move first!\n\nWhat do you do?\n1. Normal Attack does {totalopdamage} damage\n2. Wild Attack (you can double the damage but you will also take damage) details: you take {wild_attack_player_damage} the wolf takes {wild_attack_damage}\n3. Drink a healing potion (get 9 health)\n4. Flee (50% chance of surviving): ")
    if attack == 1:
        wolf_damage = random.randint(500,10000)
        print(f"You attacked the dire wolf you did {totalopdamage} but the wolf did {wolf_damage}")
        if wolf_damage >= 30:
            print("You die! wolf win")
    if attack == 2:
        print(f"You did the wild attack damage and dealt {wild_attack_damage} and you got {wild_attack_player_damage} damage")
        if wild_attack_player_damage >= 30:
            print("You die! wolf win")
        else:
            print("YOU WIN! somehow...")
    if attack == 3:
        new_health = health + 9
        print(f"You gained {new_health}")
        print(f"But the dire wolf attacked you and did {totalopdamage} damage to you so you die")
    if attack == 4:
        escape_chance = random.randint(1,2)
        if escape_chance == 1:
            print("The wolf caught upto you and you died!")
        if escape_chance == 2:
            print("You escaped! but you ran too fast and headbutted into a tree you die!")


def battle_warrior_3():
    opdamage = random.randint(1,20)
    totalopdamage = 0
    totalopdamage = opdamage + 4
    
    
    health = 25
    
    wild_attack_player_damage = random.randint(20,500)
    
    wild_attack_damage = totalopdamage * 2
    
    
    attack = input(f"You are being attacked by a dire wolf!\nYou move first!\n\nWhat do you do?\n1. Normal Attack does {totalopdamage} damage\n2. Wild Attack (you can double the damage but you will also take damage) details: you take {wild_attack_player_damage} the wolf takes {wild_attack_damage}\n3. Drink a healing potion (get 9 health)\n4. Flee (50% chance of surviving): ")
    if attack == 1:
        wolf_damage = random.randint(500,10000)
        print(f"You attacked the dire wolf you did {totalopdamage} but the wolf did {wolf_damage}")
        if wolf_damage >= 30:
            print("You die! wolf win")
    if attack == 2:
        print(f"You did the wild attack damage and dealt {wild_attack_damage} and you got {wild_attack_player_damage} damage")
        if wild_attack_player_damage >= 30:
            print("You die! wolf win")
        else:
            print("YOU WIN! somehow...")
    if attack == 3:
        new_health = health + 9
        print(f"You gained {new_health}")
        print(f"But the dire wolf attacked you and did {totalopdamage} damage to you so you die")
    if attack == 4:
        escape_chance = random.randint(1,2)
        if escape_chance == 1:
            print("The wolf caught upto you and you died!")
        if escape_chance == 2:
            print("You escaped! but you ran too fast and headbutted into a tree you die!")

#endregion

main()

