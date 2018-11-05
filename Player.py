# -*- coding: utf-8 -*-
import random
import time
from Items import Weapon
from Items import Armor

class Player:
    def __init__(self,weapon,armor):
        self.hp = 1000
        self.exp = 0
        self.lvl = 1
        self.sword = []
        self.sword.append(weapon)
        self.armor = armor

    def attack(self):
        enemy_hp = 100

        while True:
            time.sleep(0.05)
            print("-"*20)
            self.slow_print("Twoje hp " + str(self.hp) + "\nHp przeciwnika " + str(enemy_hp), 0.005)

            while True:
                for x in range(0, len(self.sword)):
                    self.slow_print(self.sword[x].name, 0.005)
                p = int(input(">>>"))  #wyskakuje blad gdy niedamy wartosci!!!!

                if p < len(self.sword) and random.randint(0, 100) < self.sword[p].chance:
                    if random.randint(1, 100) > self.sword[p].crit:
                        tmp = self.sword[p].dmg + random.randint(-10, 10)
                    else:
                        tmp = (self.sword[p].dmg + random.randint(-10, 10))*2
                    enemy_hp -= tmp
                    self.slow_print("Trafiłeś za " + str(tmp), 0.01)
                    break

                elif p > len(self.sword):
                    print("Wpisz odpowiednia liczbe\n")

                else:
                    print("Chybiłeś :(\n")
                    break

            if enemy_hp <= 0:
                tmp = random.randint(30, 60)
                self.slow_print("Wygrałeś, dostałeś " + str(tmp) + " exp\n", 0.01)
                self.update_lvl(tmp)
                break

            tmp = random.randint(10, 20)
            self.update_hp(int(tmp*(100 - self.armor.armor)/100))

    def update_lvl(self, value):
        time.sleep(0.05)
        levelup = False
        self.exp += value
        self.slow_print("Dostałeś " + str(value) + " exp", 0.005)

        while self.exp >= self.lvl * 100:
            self.exp -= self.lvl * 100
            self.lvl += 1
            levelup = True

        if levelup:
            print("*" * 20)
            self.slow_print("Nowy poziom!\nTwój poziom: " + str(self.lvl) + "\n", 0.005)
            self.hp = 100

        else:
            self.slow_print("Brakuje Ci " + str(self.lvl * 100 - self.exp) + " exp do nowego poziomu", 0.005)

    def update_hp(self, value):
        time.sleep(0.05)
        self.hp -= value
        if self.hp <= 0:
            self.slow_print("Tracisz " + str(value) + " hp", 0.005)
            print("*RIP*")
            self.slow_print("Koniec gry :(\n", 0.005)
            input("Wciśnij dowolny klawisz, aby zakończyć")
            exit(0)
        else:
            self.slow_print("Tracisz " + str(value) + " hp, pozostało Ci " + str(self.hp) + "/100 hp", 0.005)

    def change_armor(self, name, armor):
        self.armor = Armor(name, armor)

    def change_sword(self, name, dmg, chance, crit):
        self.sword.append(Weapon(name, dmg, chance, crit))

    @staticmethod
    def slow_print(string, sec):
        for i in range(len(string)):
            print(string[i], end="", flush=True)
            time.sleep(sec)
        print("\n")
