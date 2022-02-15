import random
import time

class Hero:

    def __init__(self, heroname, herolife, herodamage) -> None:
        self.__name = heroname
        self.__life = herolife
        self.__damage = herodamage

    def getName(self):
        return self.__name

    def getDamage(self):
        return self.__damage

    def getLife(self):
        return self.__life

    def setLife(self, newLife):
        self.__life = newLife

    def attack(self, enemy):
        enemy.setLife(enemy.getLife() - self.getDamage())
        print(self.getName() + " attacked " + enemy.getName() + "! now " + enemy.getName() + " life is " + str(enemy.getLife()))
        

class Mage(Hero):
    
    def __init__(self, heroname, herolife, herodamage) -> None:
        Hero.__init__(self, heroname, herolife, herodamage)
    
    def healingWord(self):
        rand = random.randint(1, 8)
        self.setLife(self.getLife() + rand)
        print("HealingWord: CURE! healed " + self.getName() + "in " + str(rand) + " hitpoints! His life now is " + str(self.getLife()) + "!" )

class Archer(Hero):

    def __init__(self, heroname, herolife, herodamage) -> None:
        Hero.__init__(self, heroname, herolife, herodamage)
    
    
    def arrowBarrage(self, enemy):
        rand = random.randint(1, 3)
        i = 0

        print("arrow barrage hitted " + str(rand) + " times!" )
        for i in range(0, rand):
            self.attack(enemy)
            i = i + 1


def main():
    heroAntenor = Mage('antenor', 20, 3)
    heroFrolo = Archer('frolo', 11, 4)

    while(True):

        if (heroFrolo.getLife() <= 0 and heroAntenor.getLife() <= 0):
            print("NO ONE WON, BOTH DIED IN PITY AND SHAME!")

        if heroFrolo.getLife() <= 0:
            print(heroAntenor.getName() + " won the match!!")
            break

        if heroAntenor.getLife() <= 0:
            print(heroFrolo.getName() + " won the match!!")
            break

        randFrolo = random.randint(1, 5)
        randAntenor = random.randint(1, 3)

        if randFrolo == 4:
             heroFrolo.arrowBarrage(heroAntenor)
        else:
             heroFrolo.attack(heroAntenor)

        time.sleep(1)

        if randAntenor == 2:
             heroAntenor.healingWord()
        else:
             heroAntenor.attack(heroFrolo)

        time.sleep(1)



if __name__ == "__main__":
    main()