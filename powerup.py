import pygame
from pygame.sprite import Sprite
from random import randint

class Powerup(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/powerup.png')
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    def update(self): #the powerup falls down the screen
        self.y += 3
        self.rect.y = self.y
        self.rect.x = self.x

        if self.y >= 600: #if it hits the bottom, it repositions itself
            self.y = -3000
            self.x = randint(100,1100)


