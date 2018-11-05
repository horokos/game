from Struktura import Struktura
from Player import Player
from Items import Weapon
from Items import Armor

import Code


print("Jesteś gotowy na przygodę?\n")
print("Wybierz klasę (1/2/3)")
print("1. Wojownik")
print("2. Mag")
print("3. Łotrzyk")

while True:
    klasa = input(">>>")

    if klasa in ["1", "2", "3"]:
        break

    else:
        print("Zła wartość")

if klasa == "1":
    weapon = Weapon("Miecz pazia", 50, 60, 5)
    armor = Armor("Zardzewiała zbroja",10)
    player = Player(weapon,armor)

elif klasa == "2":
    weapon = Weapon("Sztylet złodziejaszka", 30, 90, 3)
    armor = Armor("Skurzana tunika", 10)
    player = Player(weapon, armor)

elif klasa == "3":
    weapon = Weapon("Dębowa różdżka",70,80,10)
    armor = Armor("Stara szata",10)
    player = Player(weapon, armor)

stru = Struktura(klasa + ".txt")

Code.generate()

while True:
    stru.p_move(player)

