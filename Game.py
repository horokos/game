from Struktura import Struktura
from Player import Mage
from Player import Rouge
from Player import Warrior
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

if klasa == 1:
    player = Warrior()
if klasa == 2:
    player = Mage()
if klasa == 3:
    player = Rouge()
stru = Struktura(klasa + ".txt")

Code.generate()

while True:
    stru.p_move(player)

