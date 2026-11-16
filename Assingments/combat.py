import random

health = defense = base_defense = atk_bonus = dmg_die = dmg_bonus = 0
wolf_hp, wolf_def = 25, 12
name = ""

def user_turn():
    global health, defense, wolf_hp
    defense = base_defense
    choice = input("\n1.Attack 2.Wild(+4dmg,-2def) 3.Defend(+4def) 4.Heal(+9hp): ")
    if choice == "1" and random.randint(1, 20) + atk_bonus > wolf_def:
        wolf_hp -= random.randint(1, dmg_die) + dmg_bonus
        print("Hit!")
    elif choice == "2":
        defense -= 2
        if random.randint(1, 20) + atk_bonus > wolf_def:
            wolf_hp -= random.randint(1, dmg_die) + dmg_bonus + 4
            print("Wild Hit!")
        else:
            print("Missed!")
    elif choice == "3":
        defense += 4
        print("Defending!")
    elif choice == "4":
        health += 9
        print("Healed!")
    else:
        print("Missed / Turn ends!")
    print(f"HP -> {name}: {health} | Wolf: {wolf_hp}")

def monster_turn():
    global health
    print("\nDire Wolf attacks!")
    if random.randint(1, 20) + 4 > defense:
        health -= random.randint(1, 6) + 3
        print("Wolf hits you!")
    else:
        print("Wolf misses!")
    print(f"HP -> {name}: {health} | Wolf: {wolf_hp}")

def main():
    global name, health, base_defense, defense, atk_bonus, dmg_die, dmg_bonus
    name = input("What is your name?: ")
    while True:
        w = input("1.Fighter 2.Mage 3.Rogue: ")
        if w == "1":
            health, base_defense, atk_bonus, dmg_die, dmg_bonus = 30, 14, 3, 8, 4
            break
        elif w == "2":
            health, base_defense, atk_bonus, dmg_die, dmg_bonus = 20, 11, 5, 10, 4
            break
        elif w == "3":
            health, base_defense, atk_bonus, dmg_die, dmg_bonus = 25, 13, 4, 6, 5
            break
        print("INVALID INPUT")
    defense = base_defense
    print(f"Stats -> HP:{health} Def:{defense} Atk:D20+{atk_bonus} Dmg:D{dmg_die}+{dmg_bonus}")
    print("A Dire Wolf ambushes you! Defeat it before your HP hits 0.")
    turn = random.choice(["user", "monster"])
    print(f"{name if turn == 'user' else 'Dire Wolf'} moves first!")
    while health > 0 and wolf_hp > 0:
        if turn == "user":
            user_turn()
            turn = "monster"
        else:
            monster_turn()
            turn = "user"
    print(f"Winner: {name if health > 0 else 'Dire Wolf'}!")

main()
