import sys
import pygame
import random
import time
import os

worldx = 960
worldy = 720
fps = 40
ani = 4
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

backdrop = pygame.image.load(os.path.join('heroSprites\sprites', 'png-transparent-chicken-rooster-poultry-contact-page-chicken-web-design-animals-chicken-thumbnail.png'))
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

class Hero(pygame.sprite.Sprite):

    def __init__(self, heroname, herolife, herodamage) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
        self.__name = heroname
        self.__life = herolife
        self.__damage = herodamage
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('heroSprites\sprites', 'walk' + str(i) + '.png')).convert()
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        self.movex += x
        self.movey += y 

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            self.image = self.images[self.frame//ani]

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

def characterControl():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-steps, 0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(steps, 0)

        world.blit(backdrop, backdropbox)
        player.update()
        player_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)            

if __name__ == "__main__":
    player = Hero('frolinho', 10, 1)  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 0  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10
    characterControl()